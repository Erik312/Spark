######################################
#                                    #
# Spark.py                           #
#                                    #
# Version 2.0                        #
# Written by Erik Ramos(2021)        #
#                                    #
# ramos-development.herokuapp.com    #
# github.com/Erik312                 #
#                                    #
######################################



import urllib.request, urllib.error, urllib.parse
import tkinter


#Root/Main Title
Title = "SPARK"

#Root/Main Window
root = tkinter.Tk()
root.geometry("600x600")
root.title(Title)
root.configure(bg="black")


#Main app
def silver(site_1,site_2,site_3):
    
    print("Welcome to uptime....ping up to 3 sites for status codes....")
        
    print("Gathering status codes....")
    result1 = get_status(site_1)
    if result1 == 200:
        
        r1['text'] = result1
    else:
        r1['text'] = "ERROR: 404"
        
    print("Loading........")
    result2 = get_status(site_2)
    if result2 == 200:
        
        r2['text'] = result2
    else:
        r2['text'] = "ERROR: 404"
    print("Loading.........")
    result3 = get_status(site_3)
    if result3 == 200:
        
        r3['text'] = result3
    else:
        r3['text'] = "ERROR: 404"
    print("********END**********")

#request sites for status code
def get_status(site):
    try:
        site_name = site
        ping_site = urllib.request.urlopen(f"https://{site}")
        site_status = ping_site.getcode()
        
        
        
        
        print(f"{site_name}: {site_status}")
        return site_status
    except Exception as e:
        print(str(e))




#frame controllers
def show_frame1():
    frame2.grid_forget()
    frame1.grid()
    return

def show_frame2():
    e1String = e1.get()
    e2String = e2.get()
    e3String = e3.get()
    silver(e1String,e2String,e3String)
    e1.delete(0, 'end')
    e2.delete(0, 'end')
    e3.delete(0, 'end')
    url1['text'] = e1String
    url2['text'] = e2String
    url3['text'] = e3String
    frame1.grid_forget()
    frame2.grid()
    
    return



#frame views
#frame1
frame1 = tkinter.Frame(root, bg="black")
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)
tkinter.Label(frame1,bg="black",fg="white", text="A simple tool to check status codes of sites").grid(row=1, column=2)

tkinter.Label(frame1, text="Site 1 URL: ",bg="black", fg="white").grid(row=2, column=1)
e1 = tkinter.Entry(frame1, fg="black" )
e1.grid(row=2, column=2)
tkinter.Label(frame1, text="Site 2 URL: ", bg="black", fg="white" ).grid(row=3, column=1)
e2 = tkinter.Entry(frame1, )
e2.grid(row=3, column=2)
tkinter.Label(frame1, text="Site 3 URL: ", bg="black", fg="white").grid(row=4, column=1)
e3 = tkinter.Entry(frame1, )
e3.grid(row=4, column=2)

b1=tkinter.Button(frame1, text="GO", highlightbackground="black", command=show_frame2, height=3, width=21)
b1.grid(row=5, column=2, pady=10)

#frame2
frame2 = tkinter.Frame(root, bg="black")

tkinter.Label(frame2, text="Status output", bg="black", fg="white").grid(row=1, column=2)

url1 = tkinter.Label(frame2, text="", bg="black",fg="white")
url1.grid(row=2, column=1)
r1 = tkinter.Label(frame2, text="", bg="black", fg="white")
r1.grid(row=2,column=2)

url2 = tkinter.Label(frame2, text="", bg="black", fg="white")
url2.grid(row=3, column=1)
r2 = tkinter.Label(frame2, text="", bg="black", fg="white")
r2.grid(row=3, column=2)


url3 = tkinter.Label(frame2, text="", bg="black", fg="white" )
url3.grid(row=4 , column=1)
r3 = tkinter.Label(frame2, text="", bg="black", fg="white")
r3.grid(row=4, column=2)

tkinter.Button(frame2, text="re-check",highlightbackground="black" ,command=show_frame1, height=3, width=21).grid(row=5, column=2, pady=10)



#call first frame
frame1.grid()

if __name__=='__main__':
    root.mainloop()
