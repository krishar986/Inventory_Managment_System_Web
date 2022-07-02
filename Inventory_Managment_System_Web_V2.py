import re
import time

import tornado.ioloop
import tornado.web
from selenium import webdriver


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
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Add Page</title>
</head>
<body>
    <form action ="/Loading_Page">
	<!--The urls will be added after I load all the servers-->
<label for Item_Info>Enter the item name (please enter the full name of the item so you can exact lists when you are shopping): </label>
<input type = "text" name = "Item_Info"><br><br>
<label for Item_Info>How many boxes or bags of this do you have: </label>
<input type = "text" name = "Item_Info"><br><br>
<label for Item_Info>How many available servings do you have, please enter in terms of your previous answer: </label>
<input type = "text" name = "Item_Info"><br><br>
<label for Item_Info>How many Servings do you have left before you start to run out: </label>
<input type = "text" name = "Item_Info"><br><br>
<label for Item_Info>Please enter Max Quantity: </label>
<input type = "text" name = "Item_Info"><br><br>
<label for Item_Info>Please enter how many servings are in one unit of this item: </label>
<input type = "text" name = "Item_Info"><br><br>
<input type = "hidden" name = "Item_Info" value = "Add_Page">
<input type = "submit">
</form>
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
		web_information = self.get_arguments("Item_Info")
		print(self.get_arguments("Item_Info")[0])
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
	<form action = "/Loading_Page">
		<label for Item_Info>Please enter the Store Name?</label>
		<input type = "text" name = "Item_Info">		
		<label for Item_Info>Please enter the url for the item in this store?</label>
		<input type = "text" name = "Item_Info">
		<label for Item_Info>Please enter the css_selector for the price of the item?</label>
		<input type = "text" name = "Item_Info">
		<label for Item_Info>Do you want to enter more url information?</label>
		<input type = "checkbox" name = "Item_Info">
		<input type = "submit" value = "Add">
	<input type = "hidden" value = " """+self.get_arguments("Item_Info")[0]+""" " name = "Item_Info"><input type = "hidden" value = "Add_Url_Page" name = "Item_Info"></form>
</body>
</html>""")

class Loading_Page(tornado.web.RequestHandler):
	def get(self):
		print(self.get_arguments("Item_Info"))
		Inventory = open("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/Inventory_File.csv","r")
		updated_all_lines = Inventory.readlines()
		regex_to_remove_currency = re.compile(r'\d*\.\d{1,2}')
		def Validating_Numeric_Inputs(input_):
			try:
				int(input_)
			except ValueError:
				input_ = "error"
			else:
				input_ = int(input_)
			if input_ != "error" and input_ < 0:
				input_ = "error"
			return str(input_)


		def Open_Url(url, css_selector):
			Chrome = webdriver.Chrome("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/chromedriver")
			try:
				if "https:" not in url:
					url = "https:"+url
				Chrome.get(url)
			except Exception:
				url = Open_Url(url)
			try:
				error_message = Chrome.find_element("id","main-message")
			except Exception:
				pass
			else:
				url = "error"
			if url != "error":
				try:
					elements = Chrome.find_element("css selector",css_selector).text
				except Exception:
					css_selector = "error"
				else:
					if len(regex_to_remove_currency.findall(elements)) == 0:
						css_selector = "error"
			return [url,css_selector]
		def Go_to_Google_Maps(input_):
			Chrome = webdriver.Chrome("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/chromedriver")

			Chrome.get("https://www.google.com/maps/search/"+input_)
			error_message = Chrome.find_element("id","pane").text
			error_string = "Google Maps can't find "+input_
			if error_string not in error_message:
				return input_
			else:
				input_ = "error"
				return input_
		if self.get_arguments("Item_Info")[-1] == "Add_Page":
			web_information = self.get_arguments("Item_Info")
			web_information[1] = Validating_Numeric_Inputs(web_information[1])
			web_information[2] = Validating_Numeric_Inputs(web_information[2])
			web_information[3] = Validating_Numeric_Inputs(web_information[3])
			web_information[4] = Validating_Numeric_Inputs(web_information[4])
			web_information[5] = Validating_Numeric_Inputs(web_information[5])
			if "error" in web_information:
				next_page = "Error_Page"
			else:
				next_page = "Add_Url_Page"
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
	<form action = "/"""+next_page+""" "><input type = "submit" value = "Continue">
	<input type = "hidden" value = " """+",".join(web_information[0:-1])+""" " name = "Item_Info"></form>

	</body>
	</html>""")
		if self.get_arguments("Item_Info")[-1] == "Add_Url_Page":
			web_information = self.get_arguments("Item_Info")
			print(web_information)
			web_information[0] = Go_to_Google_Maps(web_information[0])
			css_selector_and_url = Open_Url(web_information[1],web_information[2])
			web_information[1] = css_selector_and_url[0]
			web_information[2] = css_selector_and_url[1]
			if "error" in web_information:
				next_page = "Error_Page"
				web_information.pop(0)
				web_information.pop(0)
				web_information.pop(0)
			else:
				next_page = "Home_Page"
				line = web_information[3]+","+web_information[0]+","+web_information[1]+","+web_information[2]
				print(updated_all_lines)
				print(line)
				updated_all_lines.append(line)
				Inventory.close()
				Inventory = open("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/Inventory_File.csv","w")
				Inventory.write("\n".join(updated_all_lines))
				Inventory.close()
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
	<form action = "/"""+next_page+""""><input type = "hidden" value = " """ + ",".join(web_information)+ """ " name = "Item_Info"><input type = "submit" value = "Continue"></form>


	</body>
	</html>""")
		


class Error_Page(tornado.web.RequestHandler):
    #Verified
	def get(self):
		web_information = self.get_argument("Item_Info").split(",")
		web_information.pop(-1)
		if self.get_argument("Item_Info").split(",")[-1] == "Add_Url_Page":
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
	<form action = "/Add_Url_Page""><input type = "hidden" value = " """+ ",".join(web_information)+"""" name = "Item_Info"><input type = "submit" value = "Continue"></form>
</body>
</html>""")
def make_app():
    return tornado.web.Application([("/Home_Page", Home_Page),("/Loading_Page", Loading_Page),("/Add_Page", Add_Page),("/Error_Page", Error_Page),("/Add_Url_Page", Add_Url_Page),("/Update_Page", Update_Page),("/Update_Url_Page", Update_Url_Page),("/Update_Page_2", Update_Page_2),("/Update_Page_3", Update_Page_3),("/Remove_Page", Remove_Page),("/Print_Page", Print_Page),("/Update_Available_Servings_Page", Update_Available_Servings_Page),])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
