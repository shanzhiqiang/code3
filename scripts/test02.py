import pytest,sys,os
sys.path.append(os.getcwd())

class Test02:

    def setup_class(self):
        pass

    def teardown_class(self):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    @pytest.mark.parametrize("usernae,password,code")
    def test01(self,username,password,code):
        print()