"""
Title: Rhino Layer State Batch Render
Author: Vlad
Description: The Script renders all the named views with
            and goes through all the layer states
"""
import rhinoscriptsyntax as rs
import sys

def ChangeLayerState(LayerState):
    """
    Receives a LayerState and changes
    the model to that specific LayerState
    """
    plugin = rs.GetPlugInObject("Rhino Bonus Tools")
    if plugin is not None:
        plugin.RestoreLayerState(LayerState, 0)
        return 1
    else :
        return 0

def GetLayerStates():
    """
    The function returns the LayerStates 
    that can be found in the model
    """
    plugin = rs.GetPlugInObject("Rhino Bonus Tools")
    if plugin is not None:
        MyArray = plugin.LayerStateNames
        MyArrayB = []
        MyArray = str(MyArray[1])
        Trigger = True
        while (Trigger):
            poz=MyArray.rfind("'")
            MyArray = MyArray[:poz]
            poz=MyArray.rfind("'")
            dif = MyArray[poz:]
            dif = dif[1:]
            MyArrayB.append(dif)
            MyArray = MyArray[:poz]
            if len(MyArray)<14:
                Trigger = False
        del MyArrayB[-1] #clean up the list
#        print (MyArray)
#        print (MyArrayB)q
        return MyArrayB

def GetViewNames():
    a = rs.NamedViews()
    return a
    

def ChooseFolderPath():
    """
    pick a folder to save the renderings to 
    return the folder
    """
    folder = rs.BrowseForFolder(rs.DocumentPath, "Browse for folder", "Batch Render")
    return folder

def Render(folder,view,state):
    FileName = folder +'\\'+ View +'_'+State
    rs.Command ("!_-Render")
    rs.Command ("_-SaveRenderWindowAs " + FileName)
    rs.Command ("_-CloseRenderWindow")

def ChangeView(View):
    rs.Command ("_-NamedView _Restore " + View + " _Enter", 0)

if __name__ == "__main__":
    VRay = rs.GetPlugInObject("V-Ray for Rhino")
    VRay.SetBatchRenderOn(True)  #Set Batch Render on True
    arrStates = GetLayerStates()  #initialise layer states
    arrViewNames = GetViewNames()
    folder = ChooseFolderPath()
    for State in arrStates:
        ChangeLayerState(State)
        print (State)
        for View in arrViewNames:
            ChangeView(View)
            Render(folder,View,State)

#    for View in arrViewNames:
#        ChangeView(View)
#        print (View)
#    for state in arrStates:
#        ChangeLayerState(state)
#        print state
#    print "Done"
#    Render()
    