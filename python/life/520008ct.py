#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2018-05-21 19:46:27
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : to express my love to 008ct
#       
print('\n'.join([''.join([(''.join(list(map(chr, [48, 48, 56, 99, 116])))[(x-y) % 5] if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)]))

# 运行结果
'''
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                t008ct008           t008ct008               
            08ct008ct008ct008   08ct008ct008ct008           
          008ct008ct008ct008ct008ct008ct008ct008ct0         
         008ct008ct008ct008ct008ct008ct008ct008ct008        
        008ct008ct008ct008ct008ct008ct008ct008ct008ct       
        08ct008ct008ct008ct008ct008ct008ct008ct008ct0       
        8ct008ct008ct008ct008ct008ct008ct008ct008ct00       
        ct008ct008ct008ct008ct008ct008ct008ct008ct008       
        t008ct008ct008ct008ct008ct008ct008ct008ct008c       
        008ct008ct008ct008ct008ct008ct008ct008ct008ct       
         8ct008ct008ct008ct008ct008ct008ct008ct008ct        
          t008ct008ct008ct008ct008ct008ct008ct008ct         
          008ct008ct008ct008ct008ct008ct008ct008ct0         
            ct008ct008ct008ct008ct008ct008ct008ct           
             008ct008ct008ct008ct008ct008ct008ct            
              8ct008ct008ct008ct008ct008ct008ct             
                008ct008ct008ct008ct008ct008c               
                  ct008ct008ct008ct008ct008                 
                    08ct008ct008ct008ct00                   
                       008ct008ct008ct                      
                          t008ct008                         
                             ct0                            
                              0                             
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
                                                            
[Finished in 1.2s]
'''