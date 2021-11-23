from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
<head>
<title>My Webserver</title>
</head>
<body>
<h1>TOP FIVE PROGRAMMING LANGUAGES</h1>
<h2>1.Javascript</h2>
Many languages came and disappear but JavaScript is one of those few renowned languages that is enjoying a high run and demand in the programming world. 
In the TIOBE ranking report, JavaScript has been ranked under the top 10 programming languages for several years consistently. 
In fact, the Stack Overflow survey depicts that JavaScript is the most popular language among developers. 
At Octoverse also, JavaScript is enjoying the top position among all programming languages. 
Meanwhile, some of the renowned companies in the tech world that are using JavaScript are Facebook, Google, Microsoft, Uber, etc.
<h2>2.R</h2>
R is another emerging name in the Programming world! It is an open-source programming language that is widely used in the area of Data Science, Statistical Analysis, and Machine Learning and provides you with a huge set of libraries and frameworks. The language is very much suitable for GNU/Linux and Microsoft Windows. Also, it can be easily integrated with several data processing technologies like Hadoop & Spark. Some of the other prominent features of this particular language such as cross-platform compatibility, highly extensible, strong graphical capabilities, distributed computing, etc. make it a more preferred language among the developers.
<h2>3.Java</h2>
Java is a high-level,object-oriented programming language.Java code runs on any machine that doesn’t need any special software to be installed.
 Java uses automatic memory allocation and garbage collection. It doesn't provide explicit pointers so that the programmercannot access the memory directly from the code.
<h2>4.C#</h2>
If we particularly talk about C language, the general-purpose procedural programming language is majorly used in the development of low-level systems like operating systems, kernel development, and others. 
And many other programming languages inherit the properties of this particular language. 
On the other hand, C++ is an object-oriented programming language (primarily developed as an extension of C).
 The language is widely used in Game Development, GUI & Desktop applications, and Competitive Programming along with several other fields
  <h2>5.Python</h2>
  Python has been the favorite language of almost every individual who is just starting with the programming domain for the last many years. 
  The primary reason behind this is a quite simple syntax that makes it easy to read, learn, and use. The language is extensively used for web development, software development, etc., and with several trending technologies such as Machine Learning, Artificial Intelligence, Data Science, etc.
  The language offers some enriching features such as rich library support, automatic garbage collection, easier integration with other languages, GUI Programming support, and many more. 
  Several popular Python frameworks that make things more efficient & convenient are Django, Flask, Pyramid, etc.
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()
