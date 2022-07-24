from findMatariki import Matariki
import unittest


class TestMatarikiDate(unittest.TestCase):

    def test_year_2022(self):
        self.assertEqual('2022-06-24', Matariki.getMatariki(2022))

    def test_year_2023(self):
        self.assertEqual('2023-07-14', Matariki.getMatariki(2023))

    def test_year_2024(self):
        self.assertEqual('2024-06-28', Matariki.getMatariki(2024))

    def test_year_2025(self):
        self.assertEqual('2025-06-20', Matariki.getMatariki(2025))

    def test_year_2026(self): 
        self.assertEqual('2026-07-10', Matariki.getMatariki(2026))

    def test_year_2027(self):
        self.assertEqual('2027-06-25', Matariki.getMatariki(2027))

    def test_year_2028(self):
        self.assertEqual('2028-07-14', Matariki.getMatariki(2028))

    def test_year_2029(self):
        self.assertEqual('2029-07-06', Matariki.getMatariki(2029))

    def test_year_2030(self):
        self.assertEqual('2030-06-21', Matariki.getMatariki(2030))

    def test_year_2031(self):
        self.assertEqual('2031-07-11', Matariki.getMatariki(2031))

    def test_year_2032(self):
        self.assertEqual('2032-07-02', Matariki.getMatariki(2032))

    def test_year_2033(self):
        self.assertEqual('2033-06-24', Matariki.getMatariki(2033))

    def test_year_2034(self):
        self.assertEqual('2034-07-07', Matariki.getMatariki(2034))

    def test_year_2035(self):
        self.assertEqual('2035-06-29', Matariki.getMatariki(2035))

    def test_year_2036(self):
        self.assertEqual('2036-07-18', Matariki.getMatariki(2036))

    def test_year_2037(self):
        self.assertEqual('2037-07-10', Matariki.getMatariki(2037))

    def test_year_2038(self):
        self.assertEqual('2038-06-25', Matariki.getMatariki(2038))

    def test_year_2039(self):
        self.assertEqual('2039-07-15', Matariki.getMatariki(2039))

    def test_year_2040(self):
        self.assertEqual('2040-07-06', Matariki.getMatariki(2040))

    def test_year_2041(self):
        self.assertEqual('2041-07-19', Matariki.getMatariki(2041))

    def test_year_2042(self):
        self.assertEqual('2042-07-11', Matariki.getMatariki(2042))

    def test_year_2043(self):
        self.assertEqual('2043-07-03', Matariki.getMatariki(2043))

    def test_year_2044(self):
        self.assertEqual('2044-06-24', Matariki.getMatariki(2044))

    def test_year_2045(self):
        self.assertEqual('2045-07-07', Matariki.getMatariki(2045))

    def test_year_2046(self):
        self.assertEqual('2046-06-29', Matariki.getMatariki(2046))

    def test_year_2047(self):
        self.assertEqual('2047-07-19', Matariki.getMatariki(2047))

    def test_year_2048(self):
        self.assertEqual('2048-07-03', Matariki.getMatariki(2048))

    def test_year_2049(self):
        self.assertEqual('2049-06-25', Matariki.getMatariki(2049))

    def test_year_2050(self):
        self.assertEqual('2050-07-15', Matariki.getMatariki(2050))

    def test_year_2051(self):
        self.assertEqual('2051-06-30', Matariki.getMatariki(2051))

    def test_year_2052(self):
        self.assertEqual('2052-06-21', Matariki.getMatariki(2052))


if __name__ == '__main__':
    unittest.main()
