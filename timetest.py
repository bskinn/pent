import pent, gzip, numpy as np

def timetest():
    """Run timing test with data/code of #61."""
    with gzip.open('pent\\test\\isosorbide_NO3_02.out.gz', 'rt') as f:
       data = f.read()

    prs = pent.Parser(
        head=("'@.REDUCED MASS:' #+.f", "'@.IR INTENSITY:' #+.f", ""),
        body="~ #!+.f",
        )

    cap = prs.capture_body(data)

    arr = np.column_stack(np.array(_, dtype=float) for _ in cap)

    #print(arr)

