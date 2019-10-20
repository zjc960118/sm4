# 基于SM4-ECB、CBC模式的图片加解密
## 实现思路
SM4算法是一种分组加密算法，其输入需要二进制流，并不能直接对图片进行加密处理  
因而需要对图片进行预处理，“RGBA”格式图片为32位彩色图像，它的每个像素用32个bit表示，其中24bit表示红色、绿色和蓝色三个通道，另外8bit表示alpha通道，即透明通道。转化后RGBA的图片可以直接用SM4算法进行加解密  
  
具体思路如下：  
**加密：** 先将JPG格式的图片进行格式转换成RGBA格式，再使用sm4算法进行加密，最后将加密后的RGBA图片转化为JPG  
**解密：** 先将加密后JPG格式的图片进行格式转换成RGBA格式，再使用sm4算法进行解密，最后将解密后的RGBA图片转化为JPG  

## 具体实现
### 1.在Python中对图片格式转化  
JPG转RGBA  
```
from PIL import Image
 
pku = Image.open('pku.jpg')
pku_rgba = pku.convert('RGBA')
pku_rgba.save('pku.rgba')
width1 = pku.size[0]
height1 = pku.size[1]

print(width1)
print(height1)
```
RGBA转JPG
```
pku_rgb = pku_rgba.convert('RGB')
pku_rgb.save('pku_rgb.jpg')
```

### 2.图片加密   
**2.1 安装gmssl**  
  
从 https://github.com/guanzhi/GmSSL 中下载并安装gmssl 

**2.2 基于ECB模式的加解密**  

加密  ` gmssl enc -sms4-ecb -e -in pku.rgba -out pku_ecb.rgba `  

解密  ` gmssl sms4-ebc -d -in pku_ecb.rgba -out pku_ecb_dec.rgba` 
  
**2.3 基于CBC模式的加密**  
  
加密 ` gmssl enc -sms4-cbc -e -in pku.rgba -out pku_cbc.rgba `  
  
解密  `  gmssl sms4-cbc -d -in pku_cbc.rgba -out pku_cbc_dec.rgba`  



 ### 3.运行结果  
 原图    
  
![image](https://github.com/zjc960118/sm4/blob/master/image/sm4_pku/pku.jpg)    



**3.1 基于ECB模式的加解密**    
 加密  
![image](https://github.com/zjc960118/sm4/blob/master/image/%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-10-20%20%E4%B8%8A%E5%8D%882.32.40.png)    

加密结果   

![image](https://github.com/zjc960118/sm4/blob/master/image/sm4_pku/pku_ecb.jpg)   
解密     
![image](https://github.com/zjc960118/sm4/blob/master/image/%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-10-20%20%E4%B8%8B%E5%8D%883.21.43.png)    
 
解密结果：  
![image](https://github.com/zjc960118/sm4/blob/master/image/sm4_pku/pku_ecb_dec.jpg)    

**3.2 基于CBC模式的加解密**   
加密    
![image](https://github.com/zjc960118/sm4/blob/master/image/%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-10-20%20%E4%B8%8B%E5%8D%883.22.46.png)   

加密结果    

![image](https://github.com/zjc960118/sm4/blob/master/image/sm4_pku/pku_cbc.jpg)   

解密  
![image](https://github.com/zjc960118/sm4/blob/master/image/%E8%BF%90%E8%A1%8C%E6%88%AA%E5%9B%BE/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202019-10-20%20%E4%B8%8B%E5%8D%883.22.56.png)    

解密结果：    
![image](https://github.com/zjc960118/sm4/blob/master/image/sm4_pku/pku_cbc_dec.jpg)  







