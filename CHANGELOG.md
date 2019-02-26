# Changelog



### 0.2.0 - [#4](https://github.com/openfisca/country-template/pull/4)

* Tax and benefit system evolution.
  - Added variables based on birth day: `age_in_months`, `is_birthday_past`, `birth_month`
  - Renamed `active_kids__is_entitled` to `active_kids__child_meets_criteria`
  - Added "others" role in family
  - Added 
    - `active_kids__voucher_amount`
    - `active_kids__family_has_children_eligible`
    - `active_kids__is_eligible`

### 0.1.1 - [#2](https://github.com/openfisca/country-template/pull/2)

* Technical improvement
  - Remove deployment from circle-ci

### 0.1.0 - [#1](https://github.com/openfisca/country-template/pull/1)

* Technical improvement
  - Circle ci config
