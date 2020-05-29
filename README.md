# Rhino Tool Batch Render
The tool was developed by myself for Grimshaw Architects. The purpose of the tool is to automate the rendering process. 

## How it works
It is an automation of the rendering process, which is currently still missing within Rhino 5, and it makes use of VRay 3  as the default renderer through actioning its API.  

## What it does
0) The script must be loaded from the comand line of Rhino
1) The script will then prompt for an output folder
1) The Script will itterate through all the Named Views and all the Layer States. 
2) Every rendering is then saved in the specified folder together with the pre-selected passes. 
3) The naming of the file then contains the LayerState and the Named View

## Short Info
The code is written in Python using the RhinoScript library and the VRay 3 API. 

### Contribute
- I have stopped maintaining the script as I currenly lack access to the license. 
- Please feel free to use it under the MIT Licence 
- If you have any edit suggestions, make a pull request
