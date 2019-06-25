

def  saomiao():
	commodity={
	"101":("瓜子",5.0),
	"102":("农夫山泉",2.0),
	"103":("士力架",2.0),
	"104":("健力宝",3.0),
	}
	receipt=list();
	b=1;
	lens=0;
	while  True:
		sao=input("请扫描商品条码  b 查看清单 add 添加信息 del 删除信息 updata 更新信息 end 结束购物\n");
		if sao=="end":
			break;
		elif sao=="b":
			num=0;
			d=set(receipt);
			for b in d:
				count=0;
				for rece in receipt:
					if b == rece:
 						count += 1
 						num+=float(rece[1])
				print("商品名称:%s,商品单价:%.2f,数量:%d"%(b[0],b[1],count))
			print("总价",num);
		elif sao=="add" :
			key=input("请输入商品序号:\n");
			name=input("请输入商品名称:\n");
			price=float(input("请输入商品单价:\n"));
			value="('%s',%d)"%(name,price)
			commodity[key]=eval(value);
			print(commodity)
		elif sao=="del":
			pop=input("请输入删除的key:\n")
			commodity.pop(pop);
			print(commodity)
		elif sao=="updata":
			key=input("输入key值：\n");
			print(commodity[key])
			name=input("输入商品名称:\n");
			price=float(input("输入单价:\n"));
			value="('%s',%d)"%(name,price)
			commodity[key]=eval(value)
		else:
			print("输入键无效")
		a=commodity.get(sao);
		if a :
				print("商品：%s,单价：%.2f"%a)
				receipt.append(a)
				lens=len(receipt)

def  main():
	while True:
		print("==========================================\n\t\t欢迎来到微微超市  2018-3-29\n\t\t\t\t\t\t收银系统 0.1\n\t\t\t\t技术支持电话：13800138000\n==========================================")
		choose=input("按0开始扫描，q退出:\n");
		if choose=="0":
			saomiao();
			break;
		elif choose=="q":
			print("退出");
			break;
		else: 
		 	continue;
			

#saomiao();
main();
