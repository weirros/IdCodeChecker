# IdCodeChecker
Chinese ZIIOT coding check code generater；China MA Cdoe，MA.156 UDI MA校验码；DI、PI校验码算法；MA码，IDCode,UDI校验码


## 2022年顺利起航，如果这片代码有用，记得给个星；




    from idcodechecker import map2dec
    
    dt=['MA.156.M0.100472.1110331',							#DI传参不必传最后一位，需要提前处理好
        '.S1576130942.P190101.LABS20191201.E191201'			#PI传参不必传校验字段，但是要携带带前面的点 
        ]

    for do in dt:

        cd = map2dec(do)
        print (do,' => ',cd)


    -----------
    MA.156.M0.100472.1110331  => 6
    .S1576130942.P190101.LABS20191201.E191201  => 7


http://check.idcode.net/

Thanks;

https://www.programminghunter.com/article/98401286738/
