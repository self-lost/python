
class super:
	def __init__(self,name,age,address):
		self.name=name;
		self.age=age;
		self.address=address;
	def  show(self):
		print(__name__)
		print("姓名'%s',年龄：%d,地址：'%s'"%(self.name,self.age,self.address));
	def a(a):
		print("",a)
name=input("请输入名字:\n");
age=int(input("请输入年龄\n"));
address=input("请输入地址\n");
super(name,age,address).show();
#super.a("123")
