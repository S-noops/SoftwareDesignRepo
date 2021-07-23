from server import app,logged_in
import unittest

#MADE BY Sanjay Paudel ID: 1908201

class FlaskTestCase(unittest.TestCase):


    # Ensure that Flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertIn(b'Sign In', response.data)

    # Ensure that homepage dosen't show details without login
    def test_homepage_error(self):
        tester = app.test_client(self)
        response = tester.get('/home')
        if logged_in == False:
            self.assertIn(b'Login To view content!', response.data)

    # Ensure that fuelpage dosen't show details without login
    def test_fuelpage_error(self):
        tester = app.test_client(self)
        response = tester.get('/fuel')
        if logged_in == False:
            self.assertIn(b'Login To view content!', response.data)



    # Ensure that userprofile dosen't show details without login
    def test_profilepage_error(self):
        tester = app.test_client(self)
        response = tester.get('/user')
        if logged_in == False:
            self.assertIn(b'Login To view content!', response.data)


    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login_check',
            data=dict(uname="admin", password="admin"),
            follow_redirects=True
        )
        self.assertIn(b'This is the Homepage of the app', response.data)

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client(self)
        response = tester.post(
            '/login_check',
            data=dict(uname="wrong", password="wrong"),
            follow_redirects=True
        )
        self.assertIn(b'Login Credentials Incorrect!', response.data)


    # Ensure signup behaves correctly with correct credentials
    def test_correct_signup(self):
        tester = app.test_client(self)
        response = tester.post(
            '/signup_check',
            data=dict(uname="steve", password="smith", email="steve@smith.com"),
            follow_redirects=True
        )
        self.assertIn(b'User Registration Done!', response.data)

    # Ensure signup behaves correctly with incorrect credentials
    def test_incorrect_signup(self):
        tester = app.test_client(self)
        response = tester.post(
            '/signup_check',
            data=dict(uname="admin", password="admin", email="admin@admin.com"),
            follow_redirects=True
        )
        self.assertIn(b'Duplicate Users Not Allowed!', response.data)


    # Ensure that fuelhistory dosen't show details without login
    def test_fuelhispage_error(self):
        tester = app.test_client(self)
        response = tester.get('/fuelhis')
        if logged_in == False:
            self.assertIn(b'Login To view content!', response.data)


    # Ensure that fuelqoute works properly when submit is clicked
    def test_fuel_check(self):
        tester = app.test_client(self)
        response = tester.post(
            '/fuel',
            data=dict(gallonreq=100, deldate="2020-05-24", sugprice=250, dueamount=25000, deladdress="Texas, North America"),
            follow_redirects=True
        )
        self.assertIn(b'Record Successfully Added!', response.data)

    # Ensure that userprofile works properly when submit is clicked
    def test_profile_check(self):
        tester = app.test_client(self)
        response = tester.post(
            '/user',
            data=dict(name="admin", add1="North Calorina", add2="US" ,city="Texas", state="TX", zipcode="111111"),
            follow_redirects=True
        )
        self.assertIn(b'Changes Successfully Recorded!', response.data)

    # # Ensure that after login the fuel page displays properly.
    # def test_fuel_loads(self):
    #     tester = app.test_client(self)
    #     if self.login_done == True:
    #         response = tester.get('/fuel')
    #         self.assertIn(b'Suggested Price per Gallon (USD)', response.data)

    # # Ensure that after login the fuelhis page displays properly.
    # def test_fuelhis_loads(self):
    #     tester = app.test_client(self)
    #     if self.login_done == True:
    #         response = tester.get('/fuelhis')
    #         self.assertIn(b'Suggested Price per Gallon', response.data)

    # # Ensure that after login the prodile page displays properly.
    # def test_profile_loads(self):
    #     tester = app.test_client(self)
    #     if self.login_done == True:
    #         response = tester.get('/user')
    #         self.assertIn(b'Clear', response.data)

if __name__ == '__main__':
    unittest.main()
