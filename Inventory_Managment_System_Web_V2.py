#Inventory File Structure
#Item Name, Quantity, Available Servings, Threshold, Maximum Quantity, Servings Per Unit
#Url Information Structure
#Store, Url, Css_Selector




import tornado.ioloop
import tornado.web
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from selenium import webdriver
import smtplib
import time
import re
from string import digits
import datetime


#Pages
class Home_Page(tornado.web.RequestHandler):
    #Verified
	def get(self):
		Inventory = open("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/Inventory_File.csv","r")
		all_lines = Inventory.readlines()
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
	<form action = "/Update_Available_Servings_Page"><select name = "Item_Info">""")
		for i in all_lines:
			self.write("<option value = '"+i.split(",")[0]+"'>"+i.split(",")[0]+"</option>")
		self.write("""</select><input type = "submit" value = "Update Available Servings Page"></form>
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
		Inventory = open("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/Inventory_File.csv","r")
		all_lines = Inventory.readlines()
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
	<form action = "/Loading_Page"><select name = "Item_Info">""")
		for i in all_lines:
			self.write("<option value = '"+i.split(",")[0]+"'>"+i.split(",")[0]+"</option>")
		self.write("""</select><input type = "hidden" name = "Item_Info" value = "Remove_Page"><input type = "submit" value = "Remove Item"></form>
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
	<title>Print Page</title>
</head>
<body>
	<form action = "/Loading_Page"><label>Please enter the email you want the list sent to?</label><input type = "text" name = "Item_Info"><input type = "hidden" name = "Item_Info" value = "Print_Page"><input type = "submit" value = "Print List"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")


class Update_Available_Servings_Page(tornado.web.RequestHandler):
    #Verified
	def get(self):
		Inventory = open("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/Inventory_File.csv","r")
		all_lines = Inventory.readlines()
		item_name = self.get_argument("Item_Info").split(",")[0]
		for i in all_lines:
			if i.split(",")[0] == item_name:
				available_servings = i.split(",")[2]
				available_quantity = i.split(",")[1]
		self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Update Available Servings Page</title>
</head>
<body>
	<form action = "/Loading_Page"><label>Please enter how much """+item_name+""" do you have left? Note: You currently have """+available_servings+""" servings of """+item_name+""" and """+available_quantity+""" bag(s) or box(s) of """+item_name+"""</label><input type = "text" name = "Item_Info"><input type = "hidden" name = "Item_Info" value = '"""+item_name+"""'><input type = "hidden" name = "Item_Info" value = "Update_Available_Servings_Page"><input type = "submit" value = "Update Available Servings"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")


class Update_Page_2(tornado.web.RequestHandler):
    #Verified
	def get(self):
		Inventory = open("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/Inventory_File.csv", "r")
		all_lines = Inventory.readlines()
		for i in all_lines:
			i_2 = i.replace("\n","")
			if i_2 == "":
				all_lines.remove(i)
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
	<form action = "/Update_Page_3"><select name = "Item_Info">""") 
		for i in all_lines:
			name = i.split(",")[0]
			self.write("<option value = "+'"'+name+'"'+">"+name+"</option>")

		self.write("""</select><input type = "submit" value = "Update Item Info"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")


class Update_Page_3(tornado.web.RequestHandler):
    #Verified
	def get(self):
		Inventory = open("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/Inventory_File.csv", "r")
		all_lines = Inventory.readlines()
		item_info = []
		for i in all_lines:
			if self.get_argument("Item_Info") == i.split(',')[0]:
				item_info.append(i)
				break
		item_info = item_info[0]
		self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Update Page_3</title>
	<style>
		th,td{border:1px solid black}
		</style
</head>
<body><table><tr>""")

		for i in item_info.split(","):
			self.write("<td>"+i+"</td>")
		self.write("""</tr></table><form action = "/Loading_Page">""")
		for i in item_info.split(","):
			self.write("""<label for Item_Info>What do you want to change <b><i>"""+i+"""</i></b> to?</label><input type = "text" name = "Item_Info"><br>""")
		self.write("""<input type = "hidden" name = "Item_Info" value = '"""+ item_info.split(",")[0]+"""'><input type = "hidden" name = "Item_Info" value = "Update_Page_3"><input type = "submit" value = "Update"></form>
	<form action = "/Home_Page"><input type = "submit" value = "Back"></form>
</body>
</html>""")




class Add_Url_Page(tornado.web.RequestHandler):
    #Verified
	def get(self):
		print(self.get_arguments("Item_Info")[0])
		self.write("""<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Add Url Page</title>
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
		regex_for_valid_username = re.compile(r'[A-Z,a-z,0-9,.,_,%,+,-]+@[A-Z,a-z,0-9,.,_,%,+,-]+\.[A-Z|a-z]{2,}')
		dictionary_with_all_needed_item_values = {}
		def Webscraping_Prices(css_selector_for_price, store_url):
			Chrome = webdriver.Chrome("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/chromedriver")
			Chrome.get(store_url)
			Chrome.refresh()
			time.sleep(10)
			price = Chrome.find_element("css selector",css_selector_for_price).text
			y = regex_to_remove_currency.search(price)
			Chrome.close()
			return y.group()
		def Print_List():
			list_of_prices = []
			dictionary_of_prices_and_stores = {}
			unique_id = 0

			for item in updated_all_lines:
				item = item.split(",")
				url_index = 6
				url = item[url_index].split(";")
				last_index = item.index(item[-1])

				if int(item[2]) <= int(item[3]):
					if len(item) > 6:
						while url_index <= last_index:
							url = item[url_index].split(";")
							price = Webscraping_Prices(url[2],url[1])
							list_of_prices.append(float(price))
							dictionary_of_prices_and_stores[price] = url[0]
							url_index += 1

						list_of_prices.sort()
						cheapest_price = list_of_prices[0]
						prices = list_of_prices
						stores = list(dictionary_of_prices_and_stores.values())
						price_index= prices.index(cheapest_price)
						store_with_cheapest_price = stores[price_index]
						quantity_needed = float(item[4]) - float(item[1])
						dictionary_with_all_needed_item_values[store_with_cheapest_price+str(unique_id)] = item[0]+","+str(quantity_needed)+","+str(cheapest_price)
						unique_id += 1

					elif len(item) == 6:
						url = item[url_index].split(";")
						price = Webscraping_Prices(url[2],url[1])
						quantity_needed = float(item[4]) - float(item[1])
						dictionary_with_all_needed_item_values[item[6] + str(unique_id)] = item[0]+","+str(quantity_needed)+","+str(price)
						unique_id += 1
			html_table = """
							<html>
							<head>
							<style type="text/css">
					th, td { border:1.5px;
						border-style: solid;
					}
				</style>
							<meta charset="utf-8">
							<meta name="viewport" content="width=device-width, initial-scale=1">
							</style>
							</head>
							<body>
							<table style="width:100%">
							<tr>                                
							<th>ITEM NAME</th>
							<th>RECOMMENDED STORE</th>
							<th>PRICE</th>
							<th>RECOMMENDED QUANTITY</th>
							<th>ITEM NUMBER</th>
							</tr>           
							"""
			list_of_lines = []
			dictionary_with_all_needed_item_values_sorted = sorted(dictionary_with_all_needed_item_values.items())
			translation_table = str.maketrans('', '', digits)
			for item in dictionary_with_all_needed_item_values_sorted:
				item_values = item[1].split(",")
				html_table = html_table+"<tr>"+"<td>"+item_values[0]+"</td>"+"<td>"+item[0].translate(translation_table)+"</td>"+"<td>"+item_values[2]+"</td>"+"<td>"+item_values[1]+"</td>"+"<td>"+str(dictionary_with_all_needed_item_values_sorted.index(item)+1)+"</td>"+"</tr>"
				list_of_lines.extend([item_values[0], item[0].translate(translation_table), item_values[2], item_values[1], dictionary_with_all_needed_item_values_sorted.index(item)])
				
			html_table = html_table+"</table>"+"</body>"+"</html>"
			html_file = open("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/html_file.html","w")
			html_file.write(html_table)
			html_file.close()
			Chrome = webdriver.Chrome("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/chromedriver")
			Chrome.get("file:///Users/krist/Desktop/Python/Course%20with%20Rahul%20Bahya/Inventory%20Management%20System%20Exercises/Inventory_managment_web/html_file.html")
			time.sleep(10)

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
				url = "error"
			try:
				error_message = Chrome.find_element("id","main-message")
			except Exception:
				pass
			else:
				url = "error"
			if url != "error":
				Chrome.refresh()
				time.sleep(10)
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
				if len(web_information) == 3:
					organized_web_info = [web_information[1],web_information[2]]
				else:
					organized_web_info  = [web_information[0], web_information[1]]
			else:
				organized_web_info = []
				if len(web_information) == 6:
					next_page = "Add_Url_Page"
					organized_web_info = [web_information[4],";".join([web_information[0],web_information[1],web_information[2]])]
				else:
					next_page = "Home_Page"
					organized_web_info = [web_information[3],";".join([web_information[0],web_information[1],web_information[2]])]
					if len(updated_all_lines) == 0:
						organized_web_info = ",".join(organized_web_info)
					else:
						organized_web_info = "\n"+",".join(organized_web_info)
					updated_all_lines.append(organized_web_info)
					Inventory.close()
					Inventory = open("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/Inventory_File.csv","w")
					Inventory.write("".join(updated_all_lines))
					Inventory.close()
					organized_web_info = []
		
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
	<form action = "/"""+next_page+""""><input type = "hidden" value = " """ + ",".join(organized_web_info)+ """ " name = "Item_Info"><input type = "submit" value = "Continue"></form>


	</body>
	</html>""")

		if self.get_arguments("Item_Info")[-1] == "Update_Page_3":
			web_information = self.get_arguments("Item_Info")
			web_information.pop(-1)
			item_name = web_information[-1]
			for i in updated_all_lines:
				if i.split(",")[0] == item_name:
					item_info = i
					break
			web_information.pop(-1)
			updated_item_info = item_info.split(",")
			for i in updated_item_info:
				if web_information[updated_item_info.index(i)] != "":
					updated_item_info[updated_item_info.index(i)] = web_information[updated_item_info.index(i)]
			for i in updated_item_info:
				index = updated_item_info.index(i)
				if index <= 5 and index > 1 and i != "":
					updated_item_info[index] = Validating_Numeric_Inputs(i)
				elif index > 5 and index % 3 == 0 and i != "":
					updated_item_info[index] = Go_to_Google_Maps(i)
				elif index > 5 and index % 3 == 1 and i != "":
					url_and_css_selector = Open_Url(i,updated_item_info[index+1])
					updated_item_info[index] = url_and_css_selector[0]
					updated_item_info[index+1] = url_and_css_selector[1]
			
			if "error" in updated_item_info:
				next_page = "Error_Page"
			else:
				next_page = "Home_Page"
				updated_all_lines[updated_all_lines.index(item_info)] = ",".join(updated_item_info)
				Inventory.close()
				Inventory = open("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/Inventory_File.csv", "w")
				Inventory.write("".join(updated_all_lines))
				
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
	<form action = "/"""+next_page+""""><input type = 'hidden' name = 'Item_Info' value = '"""+",".join([item_info,"Update_Page_3"])+"""'><input type = "submit" value = "Continue"></form>


	</body>
	</html>""")
		if self.get_arguments("Item_Info")[-1] == "Print_Page":
			Print_List()
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
	<form action = "/Home_Page"><input type = "submit" value = "Continue"></form>


	</body>
	</html>""")
		if self.get_arguments("Item_Info")[-1] == "Remove_Page":
			for i in updated_all_lines:
				if i.split(",")[0] == self.get_arguments("Item_Info")[0]:
					if updated_all_lines.index(i) == updated_all_lines.index(updated_all_lines[-1]):
						updated_all_lines[updated_all_lines.index(i)-1] =updated_all_lines[updated_all_lines.index(i)-1].replace("\n","")
					updated_all_lines.remove(i)
					break

			Inventory.close()
			Inventory = open("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/Inventory_File.csv","w")
			Inventory.write("".join(updated_all_lines))
			
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
	<form action = "/Home_Page"><input type = "submit" value = "Continue"></form>


	</body>
	</html>""")
		if self.get_arguments("Item_Info")[-1] == "Update_Available_Servings_Page":
			web_information = self.get_arguments("Item_Info")
			for i in updated_all_lines:
				if i.split(",")[0] == web_information[-2]:
					item_info = i.split(",")
					web_information[0] = Validating_Numeric_Inputs(web_information[0])
					if "error" not in web_information:
						item_info[2] = 	web_information[0]
						item_info[1] = str(int(web_information[0])/int(item_info[5]))
						updated_all_lines[updated_all_lines.index(i)] = ",".join(item_info)
						next_page = "Home_Page"
					else:
						next_page = "Error_Page"
						web_information.pop(0)
					break
			Inventory.close()
			Inventory = open("/Users/krist/Desktop/Python/Course with Rahul Bahya/Inventory Management System Exercises/Inventory_managment_web/Inventory_File.csv","w")
			Inventory.write("".join(updated_all_lines))
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
	<form action = "/"""+next_page+""""><input type = 'hidden' name = 'Item_Info' value = '"""+",".join(web_information)+"""'><input type = "submit" value = "Continue"></form>


	</body>
	</html>""")

class Error_Page(tornado.web.RequestHandler):
    #Verified
	def get(self):
		web_information = self.get_argument("Item_Info").split(",")
		if web_information[-1] == "Update_Page_3":
			web_information = self.get_argument("Item_Info").split(",")[0]
		else:
			web_information = self.get_argument("Item_Info").split(",")
			web_information.pop(-1)
			web_information = ",".join(web_information)
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
	<form action = "/"""+self.get_argument("Item_Info").split(",")[-1]+""""><input type = "hidden" value = " """+ web_information+"""" name = "Item_Info"><input type = "submit" value = "Continue"></form>
</body>
</html>""")
		
def make_app():
    return tornado.web.Application([("/Home_Page", Home_Page),("/Loading_Page", Loading_Page),("/Add_Page", Add_Page),("/Error_Page", Error_Page),("/Add_Url_Page", Add_Url_Page),("/Update_Page", Update_Page),("/Update_Page_2", Update_Page_2),("/Update_Page_3", Update_Page_3),("/Remove_Page", Remove_Page),("/Print_Page", Print_Page),("/Update_Available_Servings_Page", Update_Available_Servings_Page),])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
