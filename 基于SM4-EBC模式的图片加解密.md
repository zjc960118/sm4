# 基于SM4-EBC模式的图片加解密
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
原图 
![image](https://github.com/zjc960118/sm4/blob/master/image/sm4_pku/pku.jpg)

**2.1 安装gmssl**  

**2.2 基于EBC模式的加密**  
加密结果    
**2.3 基于CBC模式的加密**   
加密结果   

### 3.图片解密  
**3.1 基于EBC模式的加密**  
解密结果    
**3.2 基于CBC模式的加密**   
解密结果  






