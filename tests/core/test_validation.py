from core.validation import is_uuid, is_email, is_filename, is_hex, is_salt, is_hash, is_weak_password


class TestIsUuid:

    def test_is_uuid(self):
        assert is_uuid("1327e32c-885c-11ed-942c-00155d211f36")
        assert is_uuid("188bc27a-885c-11ed-942c-00155d211f36")
        assert is_uuid("1904713e-885c-11ed-942c-00155d211f36")

    def test_is_not_uuid(self):
        assert not is_uuid("1234")
        assert not is_uuid("1327e32c-885c-11ed1-942c-00155d211f36")
        assert not is_uuid("1327e32c-885c-11ed-942c-00155d211f3")
        assert not is_uuid("1327E32c-885c-11ed-942c-00155d211f36")
        assert not is_uuid("g327e32c-885c-11ed-942c-00155d211f36")


class TestIsEmail:

    def test_is_email(self):
        assert is_email("user@example.com")
        assert is_email("name.surname@gmail.com")
        assert is_email("12314215@pw.edu.pl")

    def test_is_not_email(self):
        assert not is_email("user@192.168.1.1")
        assert not is_email("user@gmail")
        assert not is_email("-user@example.com")


class TestIsPasswordWeak:

    def test_is_weak(self):
        assert is_weak_password("user")
        assert is_weak_password("user123456.")
        assert is_weak_password("UseRuSeRu")
        assert is_weak_password("useruser./1^")
        assert is_weak_password("USERUSERUSER./1^")
        assert is_weak_password("USERUSE123./1^")

    def test_id_not_weak(self):
        assert not is_weak_password("useR%$1234")
        assert not is_weak_password("Pa$$word8123")


class TestIsFilename:

    def test_is_filename(self):
        assert is_filename("picture.jpg")
        assert is_filename("archive.tar.gz")
        assert is_filename("script.py")

    def test_is_not_filename(self):
        assert not is_filename("no_extension")


class TestIsHex:

    def test_is_hex(self):
        assert is_hex("deadbeef")
        assert is_hex("0175056015105abbacd")

    def test_is_not_hex(self):
        assert not is_hex("DEADBEEF")
        assert not is_hex("109756x")


class TestIsSalt:

    def test_is_salt(self):
        assert is_salt("afgsASFmpN")

    def test_is_not_salt(self):
        assert not is_salt("afgsASFmpNa")
        assert not is_salt("afgsASFmp")
        assert not is_salt("123;,afds0")


class TestIsHash:

    def test_is_hash(self):
        assert is_hash("6fe6021f948f23a378d338e5aae048b05bbf2a796101e6e5b10cf15dd0917a2a")

    def test_is_not_hash(self):
        assert not is_hash("6fe6021f948f23a378d338e5aae048b05bbf2a796101e6e5b10cf15dd0917a2")
        assert not is_hash("gfe6021f948f23a378d338e5aae048b05bbf2a796101e6e5b10cf15dd0917a2a")
