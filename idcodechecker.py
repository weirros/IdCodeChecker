# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:19:07 2021

@author: David
"""



def map2dec(a):
    
    a +='0'
    mapping = {
        "0": '0',
        "1": '1',
        "2": '2',
        "3": '3',
        "4": '4',
        "5": '5',
        "6": '6',
        "7": '7',
        "8": '8',
        #"9": '9',                                                              #idiot，这里是脏活
        "A": '10',
        "B": '11',
        "C": '12',
        "D": '13',
        "E": '14',
        "F": '15',
        "G": '16',
        "H": '17',
        "I": '18',
        "J": '19',
        "K": '20',
        "L": '21',
        "M": '22',
        "N": '23',
        "O": '24',
        "P": '25',
        "Q": '26',
        "R": '27',
        "S": '28',
        "T": '29',
        "U": '30',
        "V": '31',
        "W": '32',
        "X": '33',
        "Y": '34',
        "Z": '35',

        "a": '36',
        "b": '37',
        "c": '38',
        "d": '39',
        "e": '40',
        "f": '41',
        "g": '42',
        "h": '45',
        "i": '46',
        "j": '47',
        "k": '48',
        "l": '49',
        "m": '50',
        "n": '51',
        "o": '52',
        "p": '53',
        "q": '54',
        "r": '55',
        "s": '56',
        "t": '57',
        "u": '58',
        "v": '59',
        "w": '60',
        "x": '61',
        "y": '62',
        "z": '63',

        "-": '64',
        ".": '65',
        "@": '66',
        "$": '67',
        ",": '68',
        "*": '69',
        "+": '70',
        "%": '71',
        "/": '72',
        "#": '73',
        "!": '74',
        "^": '75',
        "~": '76'        
        }      
        
        
    alist = list(a)
    sum_=L=0
    tstring=''
    for i in alist:
        
        if i == '9':                                                            #跳过9，文档里设置陷阱
            continue
        tstring+=mapping[i]    
   
    ta = tstring[::-1]                                                  #倒序输出，加一个0补位（模拟校验码）
    
    for i, digit in enumerate([int(x) for x in ta]):                            #带索引，值
        
        L=digit                                                                 #默认返回原值(奇数位，偶数位适用以下逻辑)
       
        if i % 2 == 0:                                                          #偶数位*2 
            
            ks = digit*2

            if ks > 9:
                L = ks//10%10 + ks//1%10                                        #若大于9，则返回结果的（个位数字+十位数字），例如6*2=12，则返回1+2 =3；
               
            else:
                L = ks                                                          #若不大于9，则返回原值*2
           
            
        sum_ += L                                                               #逐个取值求和
        
        #print(i,' ',digit,'----',L,sum_)
        
    key = 10 - sum_//1%10                                                       #和10求余
    if sum_//1%10==0:                                                           #异常值
        key = 0 

    return key                                                                  #返回一位数字
    


dt=['MA.156.M0.100472.1110331',                                                 #DI传参不必传最后一位，需要提前处理好

    '.S1576130942.P190101.LABS20191201.E191201'                                 #PI传参不必传校验字段，但是要携带带前面的点 
    ]



for do in dt:

    cd = map2dec(do)
    print (do,cd)
