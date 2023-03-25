from re import Pattern

from .util import U_EMPTY_STRING, U_SPACE
from .phonemetadata import NumberFormat
from .phonemetadata import PhoneMetadata
from .phonemetadata import REGION_CODE_FOR_NON_GEO_ENTITY

_SEPARATOR_BEFORE_NATIONAL_NUMBER: str
_EMPTY_METADATA: PhoneMetadata
_NATIONAL_PREFIX_SEPARATORS_PATTERN: Pattern[str]
_ELIGIBLE_FORMAT_PATTERN: Pattern[str]
_MIN_LEADING_DIGITS_LENGTH: int
_DIGIT_PLACEHOLDER: str
_DIGIT_PATTERN: Pattern[str]

def _get_metadata_for_region(region_code: str) -> PhoneMetadata: ...

class AsYouTypeFormatter:
    _default_country: str
    _current_metadata: PhoneMetadata
    _default_metadata: PhoneMetadata
    _current_output: str
    _accrued_input: str
    _accrued_input_without_formatting: str
    _formatting_template: str
    _last_match_position: int
    _current_formatting_pattern: str
    _prefix_before_national_number: str
    _should_add_space_after_national_prefix: bool
    _extracted_national_prefix: str
    _national_number: str
    _able_to_format: bool
    _input_has_formatting: bool
    _position_to_remember: int
    _original_position: int
    _is_complete_number: bool
    _is_expecting_country_calling_code: bool
    _possible_formats: list[NumberFormat]
    def __init__(self, region_code: str) -> None: ...
    def _maybe_create_new_template(self) -> bool: ...
    def _get_available_formats(self, leading_digits: str) -> None: ...
    def _narrow_down_possible_formats(self, leading_digits: str) -> None: ...
    def _create_formatting_template(self, num_format: NumberFormat) -> bool: ...
    def _get_formatting_template(self, number_pattern: str, number_format: str) -> str: ...
    def _clear(self) -> None: ...
    def clear(self) -> None: ...
    def input_digit(self, next_char: str, remember_position: bool = ...) -> str: ...
    def _attempt_to_choose_pattern_with_prefix_extracted(self) -> str: ...
    def _able_to_extract_longer_ndd(self) -> bool: ...
    def _is_digit_or_leading_plus_sign(self, next_char: str) -> bool: ...
    def _attempt_to_format_accrued_digits(self) -> str: ...
    def get_remembered_position(self) -> int: ...
    def _append_national_number(self, national_number: str) -> str: ...
    def _attempt_to_choose_formatting_pattern(self) -> str: ...
    def _input_accrued_national_number(self) -> str: ...
    def _is_nanpa_number_with_national_prefix(self) -> bool: ...
    def _remove_national_prefix_from_national_number(self) -> str: ...
    def _attempt_to_extract_idd(self) -> bool: ...
    def _attempt_to_extract_ccc(self) -> bool: ...
    def _normalize_and_accrue_digits_and_plus_sign(self, next_char: str, remember_position: bool) -> str: ...
    def _input_digit_helper(self, next_char: str) -> str: ...