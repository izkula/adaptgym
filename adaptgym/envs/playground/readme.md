### Instructions for adding a new playground.

1) Specify maze design in custom_mazes.py.
Add four variables to the bottom of the file (can use previous mazes as example).

```
mazes: location of walls (*), agents, and goals.
vars: ignored for now (for specifying floor texture)
height: specify wall heights
walls: specify wall textures
```

2) Add a new method to playgrounds.py that specifies the task using the custom_maze.
Use a name that begins with mazemultiagent, i.e. mazemultiagentName1.
   
These tasks can be used with any primary agent. 
   In this method you specify: which custom maze to use, the properties of the non-primary agents (i.e. spheros rolling around), the task and reward, and the motion policies of the non-primary agents.

3) Specify a primary agent for a task in playgrounds.py by adding a method to suite/[agent].py,
i.e. suite/sphero.py
   
4) Test that the playground looks as expected by using scripts/fiddle_env.py, by setting the 
'--task' flag in main().
   i.e. 
   
`'--task', 'admc_sphero_mazemultiagentInteract9',`

   