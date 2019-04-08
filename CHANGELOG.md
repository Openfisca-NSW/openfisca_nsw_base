# Changelog

### 0.2.2 - [#12](https://github.com/digitalnsw/openfisca-nsw/pull/12)

* Tax and benefit system evolution.
  - Corrected Active Kids max age cutoff to 19 years
* Technical improvement.
  - Change max and min age parameters for Active Kids to be in years, not months
  - Active Kids tests using birth date instead of age_in_months

### 0.2.1 - [#8](https://github.com/digitalnsw/openfisca-nsw/pull/8)

* Tax and benefit system evolution.
 - Added medicare card to eligibility criteria for Active Kids

### 0.2.0 - [#4](https://github.com/digitalnsw/openfisca-nsw/pull/4)

* Tax and benefit system evolution.
  - Added variables based on birth day: `age_in_months`, `is_birthday_past`, `birth_month`
  - Renamed `active_kids__is_entitled` to `active_kids__child_meets_criteria`
  - Added "others" role in family
  - Added
    - `active_kids__voucher_amount`
    - `active_kids__family_has_children_eligible`
    - `active_kids__is_eligible`

### 0.1.1 - [#2](https://github.com/digitalnsw/openfisca-nsw/pull/2)

* Technical improvement
  - Remove deployment from circle-ci

### 0.2.0 - [#17](https://github.com/digitalnsw/openfisca-nsw/pull/17)

* Tax and Benefit System evolution.
  - Added Family Energy Rebate eligibility criteria
* Technical improvement.
  - Refactor government cards in to one variable category

### 0.3.0 - [#19](https://github.com/digitalnsw/openfisca-nsw/pull/19)

* Tax and Benefit System evolution.
  - Added NRMA free2go programme

### 0.4.0 - [#20](https://github.com/digitalnsw/openfisca-nsw/pull/20)

* Tax and Benefit System evolution.
  - Added StEPS
  - Merged to PR 19

### 0.5.0 - [#21](https://github.com/digitalnsw/openfisca-nsw/pull/21)

* Tax and Benefit System evolution.
  - Added gas Rebate eligibility calculator
  - Added gas rebate amount calculator

### 0.6.0 - [#23](https://github.com/digitalnsw/openfisca-nsw/pull/23)

* Tax and Benefit System evolution.
- Free will preparation

### 0.7.0 - [#25](https://github.com/digitalnsw/openfisca-nsw/pull/25)

* Tax and Benefit System evolution.
  - Added seniors rebates
* Technical improvement
  - Fixed linting errors for update pycodestyle
  - Added python and YAML linters to circleci

### 0.7.1 - [#26](https://github.com/digitalnsw/openfisca-nsw/pull/26)

* Technical improvement
  - Fixed linting errors for update pycodestyle
  - Added python and YAML linters to circleci

### 0.7.2 - [#27](https://github.com/digitalnsw/openfisca-nsw/pull/27)

* Technical improvement
  - Update Makefile to use Openfisca Test, not openfisca-make-test

### 0.8.0 - [#28](https://github.com/digitalnsw/openfisca-nsw/pull/28)

* Tax and Benefit System evolution.
  - Added teenage education payments
