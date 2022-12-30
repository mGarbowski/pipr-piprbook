from core.identifiers import generate_uuid
from core.validation import is_uuid


class TestIsUuid:

    def test_matches(self):
        assert is_uuid("691a3d52-883e-11ed-bff4-00155d211f36")

    def test_does_not_match_length(self):
        assert not is_uuid("691a3d52-883e-11ed-bff4-00155d211f3")

    def test_does_not_match_charset(self):
        assert not is_uuid("691g3d52-883e-11ed-bff4-00155d211f36")


class TestGenerateUuid:

    def test_is_uuid(self):
        assert is_uuid(generate_uuid())
