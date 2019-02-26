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

### 0.1.0 - [#1](https://github.com/digitalnsw/openfisca-nsw/pull/1)

* Technical improvement
  - Circle ci config
