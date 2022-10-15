import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as ttk
from PIL import ImageTk,Image

data = pd.read_csv('treadmil-users.csv')

app = ttk.Tk()
app.geometry('600x300')
app.title('Trademil Users Analysis')

graphs = ttk.Variable(app)
#values=['Select']+list(data.columns)
values={'Data 1':'1', 'Data 2':'2'}
values = {'Pair Plot':'sns.pairplot(data= data)',
    'Joint Plot':"sns.jointplot(data=data, x='{col1}', y='{col2}')",
    'Bar Plot':"sns.barplot(data=data, x='{col1}', y='{col2}')"
    #'Box Plot':"sns.boxplot(data=data, x='{col1}', y='{col2}')"

}
graphs.set(values['Pair Plot'])
y = 10
for key, value in values.items():
    ttk.Radiobutton(app, text= key, variable=graphs, value = value).\
        place(x=10,y=y)
    y += 20    


### Option Menu 1
col1 = ttk.Variable(app)
values = ['Select','Product','Age','Gender']
col1.set(values[0])
ttk.Label(app, text = 'Column 1').place(x=100,y=10)
ttk.OptionMenu(app, col1, *values).place(x=100,y=40)

### Option Menu 2
col2 = ttk.Variable(app)
values = ['Select','Product','Age','Gender']
col2.set(values[0])
ttk.Label(app, text = 'Column 2').place(x=100,y=70)
ttk.OptionMenu(app, col2, *values).place(x=100,y=100)


## OPtion Menu 3
col3 = ttk.Variable(app)
values = ['Select','Product','Age','Gender']
col3.set(values[0])
ttk.Label(app, text = 'Column 3').place(x=100,y=130)
ttk.OptionMenu(app, col3, *values).place(x=100,y=150)


## Canvas
cnv = ttk.Canvas(app, width=200, height=200)
cnv.place(x=300, y=60)

##Label
result = ttk.Variable(app)
ttk.Label(app, textvariable=result).place(x=300, y=300)

def show():
    global img
    global cnv
    column1 = col1.get()
    column2 = col2.get()
    column3 = col3.get()

    g = graphs.get()
    if 'col1' in g:
        if column1 == 'Select':
            result.set('Column 1 must be selected')
            return
    if 'col2' in g:
        if column2 == 'Select':
            result.set('Column 2 must be selected')
            return
    if 'col3' in g:
        if column1 == 'Select':
            result.set('Column 3 must be selected')
            return                

    
    fig = plt.figure(figsize=(5,2))
    eval(graphs.get().format(col1= column1, col2 = column2, col3 = column3))
    fig.savefig('graph.png')
    img = ImageTk.PhotoImage(Image.open('graph.png').resize((200,200)))

    #print(col1.get(), col2.get(), col3.get())

    
    cnv.create_image(0,0, anchor = ttk.NW, image = img)
    result.set('Success')
    plt.show()

ttk.Button(app, text='Show', command = show).place(x=400,y=10)


app.mainloop()