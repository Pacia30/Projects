from lib.gratitudes import*

def test_gratitude_ippo():
    gratitudeippo = Gratitudes()
    gratitudeippo.add('Ippo')
    assert gratitudeippo.format() == "Be grateful for: Ippo"