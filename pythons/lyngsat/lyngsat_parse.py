#!/usr/bin/env python
# -*- coding: utf-8 -*-
from BeautifulSoup import BeautifulSoup
from BeautifulSoup import NavigableString   
import sys
import urllib2
import re
import unicodedata
import chardet
import codecs
import string
import os

class ComTool:
    def get_func(self):
        """Return the frame object for the caller's stack frame."""
        try:
            raise Exception
        except:
            f = sys.exc_info()[2].tb_frame.f_back
        return f.f_code.co_name  #[f.f_code.co_name, f.f_lineno]
    def get_line(self):            
        """Return the frame object for the caller's stack frame."""
        try:
            raise Exception
        except:
            f = sys.exc_info()[2].tb_frame.f_back
        return f.f_lineno  #[f.f_code.co_name, f.f_lineno

    def error(self, msg, func='', line=0):
        if(func == '' and line == 0):
            print "error: " + msg
        elif(func != '' and line != 0):
            print "error at: " + func +  ": " + str(line) + " : " + msg
        elif(func != ''):
            print "error at: " + func +  ": "  + msg
        elif(line != 0):
            print "error at: " + str(line) +  ": "  + msg
        sys.exit()


class LyngsatParser:
    def __init__(self):
        self.tool = ComTool()
        self.CurFreq = ''
        self.CurPol = ''
        self.CurSym = ''
        self.CurSystem = ''
        self.oldFreq = ''
        self.oldPol = ''
        self.oldSym = ''
        self.index=1
        self.ku_sat=0
        self.c_sat=0
        self.s2=0;
    

    def update_freq_sym(self, tr,outfile,outfile2,s2):
        if(None == tr or tr == ""):
            msg="tr is None"
            self.tool.error(msg, self.tool.get_func(), self.tool.get_line())
        all_td = tr.findAll('td')
        if(len(all_td) < 9):
            return []

        if(len(all_td[4].findAll('font')) <= 1):
            return []
         
        print all_td[4].findAll('font')[1].string
        if( all_td[4].findAll('font')[1].string == None):
            return []
        
        self.CurSystem = all_td[4].findAll('font')[1].string.strip().lstrip('\n').rstrip('\n')
         
        if(s2 == "0" and self.CurSystem != 'DVB-S'):
        #if(self.CurSystem != 'DVB-S2'):
            #print("Not s2 tp\n")
            return []
        
        if(all_td[5].find('font').contents[0] == '\n'): # no sym
            return []
        self.Feed =  all_td[2].findAll('font')[1]
        if(self.Feed != None ):
            if(self.Feed.find('b') != None):
                s1 = self.Feed.find('b').string
                if(s1 != None):
                    s2 = s1.lower()
                    if(s2.find("feed") != -1):
                        return []
        #self.CurArea = all_td[7].findAll('font')[0].findAll('a')[0].string.strip().lstrip('\n').rstrip('\n')
        if(len(all_td[7].findAll('font')[0].findAll('a')) > 0):
            self.CurArea = all_td[7].findAll('font')[0].findAll('a')[0].string.strip().lstrip('\n').rstrip('\n')
            s=self.CurArea.lower()
#            if(s.find("middle east") != -1):
#               return []
            if(s.find("america") != -1):
                return []
            if(s.find("spot 2") != -1):
                return []
            if(s.find("spot 3") != -1):
                return []
            if(s.find("brazil") != -1):
                return []
        #else:
        #    return []
        
        #bgcolor = all_td[5]['bgcolor'] 
        #if(bgcolor == '#ffffff'):
        #    return []
        
        freq_font = all_td[0].find('font')
        temp = freq_font.find('b').string
        if(temp == None):
            msg="Freq font node string is None"
            self.tool.error(msg, comTool.get_func(), comTool.get_line())
        self.CurFreq = temp.split()[0]
        self.CurPol = temp.split()[1]
        sym_font = all_td[5].find('font').contents[0]
        self.CurSym = sym_font.split('-')[0].lstrip('\n').lstrip()
        
        if(string.atoi(self.CurFreq) > (5150+11300)/2):
            outfile.write(str(self.index).decode("Latin-1").encode('Ascii'))
            outfile.write("=".encode('Ascii'))
            outfile.write(self.CurFreq.decode("Latin-1").encode('Ascii'))
            outfile.write(",".encode('Ascii'))
            outfile.write(self.CurPol.decode("Latin-1").encode('Ascii'))
            outfile.write(",".encode('Ascii'))
            outfile.write(self.CurSym.decode("Latin-1").encode('Ascii'))
            outfile.write("\n".encode('Ascii'))
            self.ku_sat=1            
        else:
            outfile2.write(str(self.index).decode("Latin-1").encode('Ascii'))
            outfile2.write("=".encode('Ascii'))
            outfile2.write(self.CurFreq.decode("Latin-1").encode('Ascii'))
            outfile2.write(",".encode('Ascii'))
            outfile2.write(self.CurPol.decode("Latin-1").encode('Ascii'))
            outfile2.write(",".encode('Ascii'))
            outfile2.write(self.CurSym.decode("Latin-1").encode('Ascii'))
            outfile2    .write("\n".encode('Ascii'))
            self.c_sat=1
        self.index = self.index+1
        
        #print self.CurFreq + "..." + self.CurPol + "..." + self.CurSym
        return []


    def parse_channel(self, tr):
        if(None == tr or tr == ""):
            msg="tr is None"
            self.tool.error(msg, self.tool.get_func(), self.tool.get_line())
        
        return []
        #print self.CurSystem 
        if(self.CurSystem != 'DVB-S'):
            return []
    
        all_td = tr.findAll('td')
        bgcolor = all_td[2]['bgcolor'] 
        if(bgcolor == '#ffffff'):
            return []
        
        fta_td = all_td[2]
        channel_td = all_td[0]
        pid_index_add = False
        if(len(channel_td.findAll('font')) == 0):
            pid_index_add = True
            fta_td = all_td[3]
            channel_td = all_td[1]
            
        fta_img = fta_td.find('img')
        if(fta_img == None):
            return []
        if(fta_img['src'] != 'f.gif'):
            return []
        print fta_img 
            
        radio = False;
        if(fta_img['title'].find('Radio') != -1):
            radio = True
           
        if(not radio):
            vpid_td = all_td[4]
            apid_td = all_td[5]
        else:
            apid_td = all_td[4]    
        if(pid_index_add):
            if(not radio):
                vpid_td = all_td[5]
                apid_td = all_td[6]
            else:
                apid_td = all_td[5]
        
        if(not radio):
            vpid = vpid_td.find('font').string.strip().lstrip('&nbsp;')        
        else:
            vpid = "8191";
        all_apid = []
        apid_font = apid_td.findAll('font')
        for font in apid_font:
            apid = ''

            if(font.string != None):
                apid = font.string
            #elif(font.contents[0].__class__ == BeautifulSoup.NavigableString):
            elif(isinstance(font.contents[0], NavigableString)):
                apid = font.contents[0]
            apid = apid.strip().lstrip('&nbsp;').split('&')[0].split(" ")[0]    

            if(apid != '' and apid != None):
                all_apid.append(apid)
        if(len(all_apid) == 0):
            all_apid.append("8191")
            all_apid.append("8191")
            all_apid.append("8191")
        elif(len(all_apid) == 1):
            all_apid.append("8191")
            all_apid.append("8191")
        elif(len(all_apid) == 2):
            all_apid.append("8191")
        #print all_apid     
        
        tag_channel = channel_td.find('a')
        if(tag_channel == None):
            tag_channel = channel_td.find('b')
        if(tag_channel == None):
            for font in channel_td.findAll('font'):
                if(font.string != None):
                    tag_channel = font.string
        else:
            tag_channel = tag_channel.string
        #tag_channel = unicodedata.normalize('NFKD', tag_channel).encode('ascii','ignore')
        #tag_channel = tag_channel.encode('ascii',errors='ignore')
        #print "--------------\n"
        tag_channel =  str(tag_channel)
        #print chardet.detect(tag_channel)['encoding']
        #print tag_channel.decode("Latin-1").encode('utf-8')
        #tag_channel = tag_channel.decode("Latin-1").encode('utf-8')#('Latin-1')
        channel = tag_channel.strip()
        av_flag = '1'
        if(radio):
            av_flag = '0'
            pcr_pid = all_apid[0]
        else:
            pcr_pid = vpid
                
        if(pcr_pid.encode('ascii') == "8191".encode('ascii')):
            pcr_pid = "8190"

        #result = [channel, '8191', vpid, all_apid[0], all_apid[1], all_apid[2], \
        #    pcr_pid, self.CurFreq, self.CurSym, self.CurPol, '0', '1', av_flag, 'Stereo']
   
        if(self.oldFreq != self.CurFreq or self.oldPol != self.CurPol or self.oldSym != self.CurSym):
			result = [self.CurFreq, self.CurSym, self.CurPol]
			self.oldFreq = self.CurFreq
			self.oldPol = self.CurPol
			self.oldSym = self.CurSym
        else:
            result = []
        #print result
        return result
    
    def parse_tr(self, tr,outfile,outfile2,s2):
        if(None == tr or tr == ""):
            msg="tr is None"
            self.tool.error(msg, self.tool.get_func(), self.tool.get_line())
        all_td = tr.findAll('td')
        if(len(all_td) == 1):
            return []
        else:       
            freq_font = all_td[0].findAll('font')
            if(len(freq_font) == 1):
                if(str(freq_font[0]).find('Freq.') != -1):
                    return []
                if(freq_font[0].find('b') != None and freq_font[0].find('a') == None):
                    return self.update_freq_sym(tr,outfile,outfile2,s2)
            else:
                return self.parse_channel(tr)

    def parse_lyngsat_page(self, url, outfile,sat_name,position,s2):
        self.CurFreq = ''
        self.CurPol = ''
        self.CurSym = ''
        self.CurSystem = ''        
        if(url == None or "" == url or outfile == None or outfile == ""):
            msg="parse_lyngsat_page param error"
            self.tool.error(msg, self.tool.get_func(), self.tool.get_line())

        print url
        res = urllib2.urlopen(url)
        html = res.read()
        print 'html: \n'
        print html

        #out = open(outfile, 'w')
        try:
            pos = outfile.find('.')       
            out_file1 = outfile[:pos]+'_KU'+outfile[pos:]
            out_file2 = outfile[:pos]+'_C'+outfile[pos:]
            out = open(out_file1,'w')
            out2 = open(out_file2,'w')
        except (IOError, OSError):
            pass
        #print codecs.lookup('Latin-1')
        #writer = codecs.lookup('Latin-1')[3](out)
        self.ku_sat=0
        self.c_sat=0
        
        out.write("[SATTYPE]\n".encode('Ascii'))
        out.write("1=".encode('Ascii'))
        out.write(position.encode('Ascii'))
        out.write("\n".encode('Ascii'))
        out.write("2=".encode('Ascii'))
        out.write(sat_name.encode('Ascii'))
        out.write("_KU".encode('Ascii'))
        out.write("\n".encode('Ascii'))
        out.write("[DVB]".encode('Ascii'))
        out.write("\n".encode('Ascii'))
        
        out2.write("[SATTYPE]\n".encode('Ascii'))
        out2.write("1=".encode('Ascii'))
        out2.write(position.encode('Ascii'))
        out2.write("\n".encode('Ascii'))
        out2.write("2=".encode('Ascii'))
        out2.write(sat_name.encode('Ascii'))
        out2.write("_C".encode('Ascii'))
        out2.write("\n".encode('Ascii'))
        out2.write("[DVB]".encode('Ascii'))
        out2.write("\n".encode('Ascii'))
        
        
        self.index = 1
        soup = BeautifulSoup(''.join(html))
        all_table = soup.findAll('table', width='720', cellspacing='0', cellpadding='0')
        for table in all_table:
            #print "------table----------"
            child_table = table.findAll('table')
            if(len(child_table) != 0):
                continue
            #print "------parse table----------"
            all_tr =table.findAll('tr')
            if(len(all_tr) <= 1):
                continue
            #    print len(tr)
            #print len(table)
            for tr in all_tr:
                result = self.parse_tr(tr,out,out2,s2)
               # if(len(result) > 0):
               #     for i in result:
               #         out.write(i.decode("Latin-1").encode('Ascii'))
               #         out.write("\t".encode('Ascii'))
               #     out.write("\n".encode('Ascii'))
        out.write("[UPDATE]\n".encode('Ascii'))
        out.close()
        out2.write("[UPDATE]\n".encode('Ascii'))
        out2.close()
        
        if(self.c_sat == 0):
            os.remove(out_file2)
        if(self.ku_sat == 0):
            os.remove(out_file1)
            

need_parse = (
                #("http://www.lyngsat.com/Eutelsat-Hot-Bird-13A-13B-13C.html","Hotbird.ini","Hot Bird 6/8/9","130"),
                #("http://www.lyngsat.com/Astra-1H-1KR-1L-1M-2C.html", "astra19_list.ini","Astra 1", "192"),
                #("http://www.lyngsat.com/Amos-2-3.html", "Amos23_list.ini","Amos 2/3", "3560"),
                #("http://www.lyngsat.com/Thor-5-6-and-Intelsat-10-02.html", "Thor56_list.ini","Thor 5/6", "3592"),
                #("http://www.lyngsat.com/Eutelsat-5-West-A.html", "Atlantic_Bird3.ini","Atlantic Bird 3", "3550"),
                #("http://www.lyngsat.com/Nilesat-101-102-201-and-Eutelsat-7-West-A.html", "nilesat.ini","Nilesat", "3530"),
                #("http://www.lyngsat.com/Express-AM44.html", "Express_AM44.ini","Express AM44","3490"),
                #("http://www.lyngsat.com/Eutelsat-12-West-A.html", "Atlantic_Bird_1.ini","Atlantic Bird 1", "3475"),
                #("http://www.lyngsat.com/Telstar-12.html", "Telstar_12.ini","Telstar 12", "3450"),
                #
                #("http://www.lyngsat.com/Intelsat-901.html", "Intelsat_901.ini","Intelsat 901", "3420"),
                #("http://www.lyngsat.com/NSS-5.html", "NSS_5.ini","NSS 5", "3400"),
                #("http://www.lyngsat.com/NSS-7-and-SES-4.html", "NSS_7.ini","NSS 7", "3380"),
                #("http://www.lyngsat.com/Intelsat-907.html", "Intelsat_907.ini","Intelsat 907", "3325"),
                #("http://www.lyngsat.com/Hispasat-1C-1D-1E.html", "Hispasat_1C_1D_1E.ini","Hispasat 1C/1D/1E", "3300"),
                #("http://www.lyngsat.com/Intelsat-903.html", "Intelsat_03.ini","Intelsat 903", "3255"),
                #("http://www.lyngsat.com/NSS-10-and-Telstar-11N.html", "NSS_10_Telstar_11N.ini","NSS 10 & Telstar 11N", "3225"),
                #("http://www.lyngsat.com/Astra-1D-and-NSS-806.html", "nss806.ini","NSS 806", "3195"),
                #
                #("http://www.lyngsat.com/Intelsat-11.html", "Intel11.ini","Intel 11", "3169"),
                #("http://www.lyngsat.com/Intelsat-14.html", "Intel14.ini","Intel 14", "3150"),
                #("http://www.lyngsat.com/Intelsat-707.html", "Intel707.ini","Intel 707", "3070"),
                #("http://www.lyngsat.com/Intelsat-805-and-Galaxy-11.html", "Intel55.ini","Iintel 55", "3045"),
                #("http://www.lyngsat.com/intel58.html", "Intel58.ini","Intel 58", "3020"),
                #("http://www.lyngsat.com/Intelsat-9-16.html", "Atlantic_Bird_2.ini","Atlantic Bird 2", "3520"),
                #("http://www.lyngsat.com/Eutelsat-3C-and-Rascom-QAF-1R.html", "Rascom QAF 1R.ini","Rascom QAF 1R", "028"),
                #("http://www.lyngsat.com/Astra-4A.html", "Astra4a.ini","Astra 4A", "048"),
                #
                #("http://www.lyngsat.com/Eutelsat-7A.html", "Eutelsat_W3A.ini","Eutelsat W3A", "070"),
                #("http://www.lyngsat.com/Eutelsat-9A-and-Ka-Sat-9A.html", "Eutelsat9A.ini","Eutelsat 9A", "090"),
                #("http://www.lyngsat.com/Eutelsat-10A.html", "Eutelsat W2A.ini","Eutelsat W2A", "100"),
                #("http://www.lyngsat.com/Eutelsat-16B.html", "Eurobird 16.ini","Eurobird 16", "158"),
                #("http://www.lyngsat.com/Arabsat-5C.html", "Arabsat 5C.ini","Arabsat 5C", "200"),
                #("http://www.lyngsat.com/Eutelsat-21A.html", "Eutelsat W6.ini","Eutelsat W6", "216"),
                #("http://www.lyngsat.com/Astra-3A-3B-and-Thor-2.html", "Astra_3A_3B_Thor_2.ini","Astra 3A/3B & Thor 2 ", "235"),
                #("http://www.lyngsat.com/Eutelsat-25A.html", "Eurobird_2.ini","Eurobird 2", "255"),
                #
                #("http://www.lyngsat.com/Eutelsat-28A-and-Astra-1N-2A-2B.html", "Eurobird 1 & Astra_1N_2A_2B_2D.ini","Eurobird 1 & Astra 1N/2A/2B/2D", "282"),
                #("http://www.lyngsat.com/Arabsat-5A.html", "Arabsat 5A.ini","Arabsat 5A", "305"),
                #("http://www.lyngsat.com/Astra-1G.html", "Astra_1G.ini","Astra 1G", "315"),
                #("http://www.lyngsat.com/Eutelsat-33A-and-Intelsat-New-Dawn.html", "Eurobird3_Intelsat_New_Dawn.ini","Eurobird 3 & Intelsat New Dawn", "330"),
                #("http://www.lyngsat.com/Eutelsat-36A-36B.html", "Eutelsat_W4_W7.ini","Eutelsat W4/W7", "360"),
                #("http://www.lyngsat.com/Paksat-1R.html", "Paksat_1R.ini","Paksat 1R", "380"),
                #("http://www.lyngsat.com/Badr-4-5-6.html", "Badr_4_5_6.ini","Badr 4/5/6 ", "260"),
                #("http://www.lyngsat.com/Hellas-Sat-2.html", "Hellas_Sat_2.ini","Hellas Sat 2", "390"),
                #
                #("http://www.lyngsat.com/Express-AM1.html", "Express_AM1.ini","Express AM1", "400"),
                #("http://www.lyngsat.com/Turksat-2A-3A.html", "Turksat_2A_3A.ini","Turksat 2A/3A", "420"),
                #("http://www.lyngsat.com/Intelsat-12.html", "Intelsat_12.ini","Intelsat 12", "450"),
                #("http://www.lyngsat.com/Yamal-202.html", "Yamal_202.ini","Yamal 202", "490"),
                #("http://www.lyngsat.com/Express-AM22.html", "Express_AM22.ini","Express AM22", "530"),
                #("http://www.lyngsat.com/Bonum-1.html", "Bonum_1.ini","Bonum 1", "560"),
                #("http://www.lyngsat.com/NSS-12.html", "NSS_12.ini","NSS 12", "570"),
                #("http://www.lyngsat.com/Intelsat-904.html", "Intelsat_904.ini","Intelsat 904 ", "600"),
                #
                #("http://www.lyngsat.com/Intelsat-902.html", "Intelsat_902.ini","Intelsat 902", "620"),
                #("http://www.lyngsat.com/Intelsat-906.html", "Intel_906.ini","Intel 906.", "642"),
                #("http://www.lyngsat.com/Intelsat-7-10.html", "Intelsat_7_10.ini","Intelsat 7/10", "685"),
                #("http://www.lyngsat.com/Insat-3C-4CR.html", "Insat_3C_4CR.ini","Insat 3C/4CR", "740"),
                #("http://www.lyngsat.com/Apstar-2R.html", "Apstar_2R.ini","Apstar 2R", "765"),
                #("http://www.lyngsat.com/Express-AM2-MD1.html", "Express_AM2_MD1.ini","Express AM2/MD1", "800"),
                #("http://www.lyngsat.com/Yamal-201.html", "Yamal_201.ini","Yamal 201", "900"),
                #
                #("http://www.lyngsat.com/Insat-2E-4A.html", "Insat_2E_4A.ini","Insat 2E/4A", "830"),
                #("http://www.lyngsat.com/Insat-3A-4B.html", "Insat_3A_4B.ini","Insat 3A/4B", "935"),
                #("http://www.lyngsat.com/NSS-6.html", "NSS_6.ini","NSS 6", "950"),
                #("http://www.lyngsat.com/AsiaSat-5.html", "AsiaSat_5.ini","AsiaSat 5", "1005"),
                #("http://www.lyngsat.com/Thaicom-5.html", "Thaicom_5.ini","Thaicom 5", "785"),
                #("http://www.lyngsat.com/AsiaSat-3S.html", "AsiaSat_3S.ini","AsiaSat 3S", "1050"),
                #("http://www.lyngsat.com/Eutelsat-16A.html", "Eutelsat_W3C.ini","Eutelsat W3C", "160"),      
                #("http://www.lyngsat.com/ABS-1.html", "ABS1_75.ini","ABS1", "750"),
             )

def main():
    parse = LyngsatParser()
    args = sys.argv
    if(len(args)==2):
        s2 = args[1]
    else:
        s2 = "1"

    fileHandle = open ( 'config.txt' )
    for line in fileHandle:
        #print line
        strlist = line.split(',')
        if(len(strlist) < 4):
            continue
        
        value0 = strlist[0]
        value1 = strlist[3]+strlist[1]
        value2 = strlist[2]
        value3 = strlist[3]
        if(value0[0] == '#'):
            continue
        print line
        print("processing")
        parse.parse_lyngsat_page(value0,value1,value2,value3,s2)

    fileHandle.close()
    #parse.parse_lyngsat_page("http://www.lyngsat.com/turk42.html", "turk42_list.txt") 
    #for need in need_parse:
    #    print "processing  " + need[0] 
    #    parse.parse_lyngsat_page(need[0], need[1],need[2],need[3])    
        
if __name__ == "__main__":
    main()
