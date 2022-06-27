from ast import Load
import tornado.web
import tornado.ioloop



#Pages
class Home_Page(tornado.web.RequestHandler):
    #Verified
    def get(self):
        self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Home Page</title>
</head>
<body>
	<form action = "/Add_Page"><input type = "submit" value = "Add Items"></form>
	<form action = "/Update_Page"><input type = "submit" value = "Update Page"></form>
	<form action = "/Remove_Page"><input type = "submit" value = "Remove Page"></form>
	<form action = "/Print_Page"><input type = "submit" value = "Print Page"></form>
	<form action = "/Update_Available_Servings_Page"><input type = "submit" value = "Update Available Servings Page"></form>
</body>
</html>""")

class Add_Page(tornado.web.RequestHandler):
    #Verified
    def get(self):
        self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Add Page</title>
</head>
<body>
	<h1>Add_Page</h1>
	<form action = "/Loading_Page"><input type = "submit" value = "Add Items"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")


class Update_Page(tornado.web.RequestHandler):
    #Verified
    def get(self):
        self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Update Page</title>
</head>
<body>
	<h1>Update_Page</h1>
	<form action = "/Update_Page_2"><input type = "submit" value = "Update Items"></form>
    <form action = "/Add_Page"><input type = "submit" value = "Add Items"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")


class Remove_Page(tornado.web.RequestHandler):
    #Verified
    def get(self):
        self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Remove Page</title>
</head>
<body>
	<h1>Remove_Page</h1>
	<form action = "/Loading_Page"><input type = "submit" value = "Remove Item"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")


class Print_Page(tornado.web.RequestHandler):
    #Verified
    def get(self):
        self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Remove Page</title>
</head>
<body>
	<h1>Print_Page</h1>
	<form action = "/Loading_Page"><input type = "submit" value = "Print List"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")


class Update_Available_Servings_Page(tornado.web.RequestHandler):
    #Verified
    def get(self):
        self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Update Available Servings Page</title>
</head>
<body>
	<h1>Update Available Servings Page</h1>
	<form action = "/Loading_Page"><input type = "submit" value = "Update Available Servings"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")


class Update_Page_2(tornado.web.RequestHandler):
    #Verified
    def get(self):
        self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Update Page</title>
</head>
<body>
	<h1>Update_Page_2</h1>
	<form action = "/Update_Page_3"><input type = "submit" value = "Update Item Info"></form>
    <form action = "/Update_Url_Page"><input type = "submit" value = "Update Url Info"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")


class Update_Page_3(tornado.web.RequestHandler):
    #Verified
    def get(self):
        self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Update Page_3</title>
</head>
<body>
	<h1>Update_Page_2</h1>
	<form action = "/Loading_Page"><input type = "submit" value = "Update"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")


class Update_Url_Page(tornado.web.RequestHandler):
    #Verified
    def get(self):
        self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Update Url Page</title>
</head>
<body>
	<h1>Update Url Page</h1>
	<form action = "/Loading_Page"><input type = "submit" value = "Update"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")


class Add_Url_Page(tornado.web.RequestHandler):
    #Verified
    def get(self):
        self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Update Url Page</title>
</head>
<body>
	<h1>Add Url Page</h1>
    <input type = "checkbox" name = "Item_Info">
	<form action = "/Loading_Page"><input type = "submit" value = "Add"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")

class Loading_Page(tornado.web.RequestHandler):
    def get(self):
        self.write("""<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
.loader {
  border: 16px solid #f3f3f3;
  border-radius: 50%;
  border-top: 16px solid #3498db;
  width: 120px;
  height: 120px;
  -webkit-animation: spin 2s linear infinite; 
  animation: spin 2s linear infinite;
}

@-webkit-keyframes spin {
  0% { -webkit-transform: rotate(0deg); }
  100% { -webkit-transform: rotate(360deg); }
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
</head>
<body>

<div class="loader"></div>
<form action = "/Input_Page"><input type = "submit" value = "Continue"></form>

</body>
</html>""")


class Error_Page(tornado.web.RequestHandler):
    #Verified
    def get(self):
        self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Error Page</title>
</head>
<body>
	<h1>Error Page</h1>
	<form action = "/Loading_Page"><input type = "submit" value = "Continue"></form>
</body>
</html>""")
def make_app():
    return tornado.web.Application([("/Home_Page", Home_Page),("/Loading_Page", Loading_Page),("/Add_Page", Add_Page),("/Error_Page", Error_Page),("/Add_Url_Page", Add_Url_Page),("/Update_Page", Update_Page),("/Update_Url_Page", Update_Url_Page),("/Update_Page_2", Update_Page_2),("/Update_Page_3", Update_Page_3),("/Remove_Page", Remove_Page),("/Print_Page", Print_Page),("/Update_Available_Servings_Page", Update_Available_Servings_Page),])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()