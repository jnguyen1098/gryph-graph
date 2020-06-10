# Gryph-Graph

This is my attempt to make use of my [Wyvern](https://github.com/jnguyen1098/wyvern) project.

This project is very coupled with Wyvern and will only take in .CSV files created using it. I have added it as a submodule.

Prior to using Gryph Graph, you need to scrape the requisite data using Wyvern. You can just specify an output name (see below) and `wyvern.py` should be able to use the default URL. At the time of writing, this URL works. Manually specifying the URL will only become relevant in the future if the Guelph website changes. If you don't want to make a new scrape, there exists a pre-made `courses.csv` in the repo. 

```
python3 wyvern/wyvern.py courses.csv
```


Assuming you executed that last step and the names of the output files you want is `outputname`, you would run it as the following.

```
python3 graph.py courses.csv output
```

`graph.py` will take your .CSV and create:

- A dotfile representation of the dependency graph (output.gv)

- An SVG file of it (output.svg), and

- A PNG of it (output.png)

You may execute both of the above commands in tandem using the `makefile`:

```
make run
```

There are a lot of things in both Wyvern and GryphGraph that I want to work on. So far the only way to really narrow down a faculty is to manually edit the CSV in Excel. Fortunately with the number of [parameters](https://github.com/jnguyen1098/wyvern) I scraped, it should hopefully be suitable for basic cases.