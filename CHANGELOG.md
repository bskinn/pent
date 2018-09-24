## CHANGELOG: pent - Pent Extracts Numerical Text

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

### [Unreleased]

...


### v0.1.0 [2018-09-23]

#### Features

 * Three token types implemented to date: numeric, string-literal, "any"
 * Parsing of multiple levels of recursive nested data; tested only
   to two leves of nesting to date.
 * Each nested level of structure can have head/body/tail
 * Captured tokens can be easily retrieved from head/tail at the top level
   parser; no good head or tail capture yet from within nested structures
