import unittest
from getMatariki import getMatariki
from yearToLunation import getLunation

# print(fr'def test_lunation_2022(self):\n
#    self.assertEqual(1230, getLunation(2022))')

class TestMatarikiDate(unittest.TestCase):
  def test_year_2022(self):
      self.assertEqual('2022-06-24', getMatariki(2022))
  def test_year_2023(self):
      self.assertEqual('2023-07-14', getMatariki(2023))
  def test_year_2024(self):
      self.assertEqual('2024-06-28', getMatariki(2024))
  def test_year_2025(self):
      self.assertEqual('2025-06-20', getMatariki(2025))
  def test_year_2026(self):
      self.assertEqual('2026-07-10', getMatariki(2026))
  def test_year_2027(self):
      self.assertEqual('2027-06-25', getMatariki(2027))
  def test_year_2028(self):
      self.assertEqual('2028-07-14', getMatariki(2028))
  def test_year_2029(self):
      self.assertEqual('2029-07-06', getMatariki(2029))
  def test_year_2030(self):
      self.assertEqual('2030-06-21', getMatariki(2030))
  def test_year_2031(self):
      self.assertEqual('2031-07-11', getMatariki(2031))
  def test_year_2032(self):
      self.assertEqual('2032-07-02', getMatariki(2032))
  def test_year_2033(self):
      self.assertEqual('2033-06-24', getMatariki(2033))
  def test_year_2034(self):
      self.assertEqual('2034-07-07', getMatariki(2034))
  def test_year_2035(self):
      self.assertEqual('2035-06-29', getMatariki(2035))
  def test_year_2036(self):
      self.assertEqual('2036-07-18', getMatariki(2036))
  def test_year_2037(self):
      self.assertEqual('2037-07-10', getMatariki(2037))
  def test_year_2038(self):
      self.assertEqual('2038-06-25', getMatariki(2038))
  def test_year_2039(self):
      self.assertEqual('2039-07-15', getMatariki(2039))
  def test_year_2040(self):
      self.assertEqual('2040-07-06', getMatariki(2040))
  def test_year_2041(self):
      self.assertEqual('2041-07-19', getMatariki(2041))
  def test_year_2042(self):
      self.assertEqual('2042-07-11', getMatariki(2042))
  def test_year_2043(self):
      self.assertEqual('2043-07-03', getMatariki(2043))
  def test_year_2044(self):
      self.assertEqual('2044-06-24', getMatariki(2044))
  def test_year_2045(self):
      self.assertEqual('2045-07-07', getMatariki(2045))
  def test_year_2046(self):
      self.assertEqual('2046-06-29', getMatariki(2046))
  def test_year_2047(self):
      self.assertEqual('2047-07-19', getMatariki(2047))
  def test_year_2048(self):
      self.assertEqual('2048-07-03', getMatariki(2048))
  def test_year_2049(self):
      self.assertEqual('2049-06-25', getMatariki(2049))
  def test_year_2050(self):
      self.assertEqual('2050-07-15', getMatariki(2050))
  def test_year_2051(self):
      self.assertEqual('2051-06-30', getMatariki(2051))
  def test_year_2052(self):
      self.assertEqual('2052-06-21', getMatariki(2052))


class TestLunationNumber(unittest.TestCase):
    def test_lunation_2022(self):
        self.assertEqual(1230, getLunation(2022))

    def test_lunation_2023(self):
        self.assertEqual(1243, getLunation(2023))

    def test_lunation_2024(self):
        self.assertEqual(1255, getLunation(2024))

    def test_lunation_2025(self):
        self.assertEqual(1267, getLunation(2025))

    def test_lunation_2026(self):
        self.assertEqual(1279, getLunation(2026))

    def test_lunation_2027(self):
        self.assertEqual(1292, getLunation(2027))

    def test_lunation_2028(self):
        self.assertEqual(1305, getLunation(2028))

    def test_lunation_2029(self):
        self.assertEqual(1317, getLunation(2029))

    def test_lunation_2030(self):
        self.assertEqual(1329, getLunation(2030))

    def test_lunation_2031(self):
        self.assertEqual(1342, getLunation(2031))

    def test_lunation_2032(self):
        self.assertEqual(1354, getLunation(2032))

    def test_lunation_2033(self):
        self.assertEqual(1366, getLunation(2033))

    def test_lunation_2034(self):
        self.assertEqual(1379, getLunation(2034))

    def test_lunation_2035(self):
        self.assertEqual(1391, getLunation(2035))

    def test_lunation_2036(self):
        self.assertEqual(1404, getLunation(2036))

    def test_lunation_2037(self):
        self.assertEqual(1416, getLunation(2037))

    def test_lunation_2038(self):
        self.assertEqual(1428, getLunation(2038))

    def test_lunation_2039(self):
        self.assertEqual(1441, getLunation(2039))

    def test_lunation_2040(self):
        self.assertEqual(1453, getLunation(2040))

    def test_lunation_2041(self):
        self.assertEqual(1466, getLunation(2041))

    def test_lunation_2042(self):
        self.assertEqual(1478, getLunation(2042))

    def test_lunation_2043(self):
        self.assertEqual(1490, getLunation(2043))

    def test_lunation_2044(self):
        self.assertEqual(1502, getLunation(2044))

    def test_lunation_2045(self):
        self.assertEqual(1515, getLunation(2045))

    def test_lunation_2046(self):
        self.assertEqual(1527, getLunation(2046))

    def test_lunation_2047(self):
        self.assertEqual(1540, getLunation(2047))

    def test_lunation_2048(self):
        self.assertEqual(1552, getLunation(2048))

    def test_lunation_2049(self):
        self.assertEqual(1564, getLunation(2049))

    def test_lunation_2050(self):
        self.assertEqual(1577, getLunation(2050))

    def test_lunation_2051(self):
        self.assertEqual(1589, getLunation(2051))

    def test_lunation_2052(self):
        self.assertEqual(1601, getLunation(2052))


if __name__ == '__main__':
    unittest.main()
