def ip_checkv4(ip):
        parts=ip.split(".")
        if len(parts)<4 or len(parts)>4:
            return False
        else:
            while len(parts)== 4:
                a=int(parts[0])
                b=int(parts[1])
                c=int(parts[2])
                d=int(parts[3])
                if a<= 0 or a == 127 :
                    return False
                elif d == 0:
                    return False
                elif a>=255:
                    return False
                elif b>=255 or b<0: 
                    return False
                elif c>=255 or c<0:
                    return False
                elif d>=255 or c<0:
                    return False
                else:
                    return True
        
        return False

def split(ip):
    parts=ip.split(".")
    return parts

def decimalToBinary(n):
    k=int(n)
    return bin(k).replace("0b", "")
    
def convertToBinary(ipv4):
    store=[]
    parts = split(ipv4)
    for i in range(len(parts)):
        store.append(str(decimalToBinary(parts[i])))
    
    string=""
    for i in range(4):
        if(i==0):
            string=string+store[i];  
        else:
            string=string+"."+store[i];
    
    return string
        
def decimalToOctal(n):
    k=int(n)
    return oct(k)
    
def convertToOctal(ipv4):
    store=[]
    parts = split(ipv4)
    for i in range(len(parts)):
        store.append(str(decimalToOctal(parts[i])))
    
    string=""
    for i in range(4):
        if(i==0):
            string=string+store[i];  
        else:
            string=string+"."+store[i];
    
    return string

def decimalToHex(n):
    k=int(n)
    return hex(k)
    
def convertToHex(ipv4):
    store=[]
    parts = split(ipv4)
    for i in range(len(parts)):
        store.append(str(decimalToHex(parts[i])))
    
    string=""
    for i in range(4):
        if(i==0):
            string=string+store[i];  
        else:
            string=string+"."+store[i];
    
    return string
    

def main():
    arr=[]
    length = 10
    storage=[]
    flag=True
    print("Enter 10 IP Address\n")
    
    for i in range(length):
        val=input()
        if(ip_checkv4(val)==True):
            arr.append(val)
        else:
            print("Not a valid IP")
            flag=False
            break
            
    if(flag==True):
        for i in range(length):
         storage.append(arr[i]+"  "+convertToBinary(arr[i])+"  "+convertToOctal(arr[i])+"  "+convertToHex(arr[i]));
    
        #print(*storage, sep='\n')
    
        file = open("conversion.txt", "w+")
        file.write('\n'.join(storage))
        file.close()
    
        # file = open("conversion.txt", "r")
        # content = file.read()
        # print(content)
        # file.close()
        sequence=["first","second","third","fourth","fifth","sixth","seventh","eight","ninth","tenth"]
        i=0
        a_file = open("conversion.txt")
        lines = a_file. readlines()
        for line in lines:
            print("The "+sequence[i]+" IP address in Decimal, Binary, Octal and hexadecimal format is "+line)
            i=i+1
        a_file. close()
    
    
    
if __name__ == "__main__":
    main()
