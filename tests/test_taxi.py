import taxi


def test_process_file():
    assert taxi.process_file("./resource/testData.txt") == """收费6元
收费7元
收费13元
收费7元"""
