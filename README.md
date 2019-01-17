# TouchDesigner Tools - Release Collection
*a collection of stand-alone tools packaged as TOX components*  
[matthew ragan](https://matthewragan.com)  

## Dependencies
* wget - python install from command line with:  
`pip install wget`  

## Summary
There are a number of tools I've worked on over the years and while it often seems obvious to me where they are, or how to download them I realized that isn't the case for everyone. This repository aims to be a collection of those tools as stand-alone TOX files. I'm working to get my own development strategy house in order, and to that end the TOX files you find here should all have release versions, and be stand-alone. That is to say that each one of them should be a tool that you can drop into your network without any fuss. Some of these components do have dependencies on external python libraries, and there are a few rules you have to follow for them to work correctly.

## Project Set-up
* Ensure that you've installed Python 3.4.5 on your computer (this is the stand alone installation of Python other than what's packaged with Touch)
* Before dropping one of these TOX files into your project make sure you've saved the TOE file in a new directory - prefferably with a descriptive name.
* when naming your directories, skip white space if possible - it just sovles so many problems. For example use something like:  
`my_great_project` or `my-great-project`  
not  
`my great project`

## Collected Components

### [hueControl]()
*additional contributors*  
[zoe sandoval](https://zoesandoval.com)

*summary*  
Philips Hue smart lights are intended to be used in homes / studios. The devices come in many varieties - individual lamps, outdoor lights, LED strip lights, etc. These are synchronized by communicating with an additional device called a Bridge. A single Bridge can control up to 50 lights. There are many stand alone applications to drive Hue Lights, and this repo aims to provide some additional control by exposing those controls through TouchDesigner. In order to do this, we use the `phue` library. There is some additional set-up required in order to use an external library, though hopefully much of this is now streamlined.

This TOX provides global control for all lights, or individual control for single lights.

### [base_save]()
*summary*  
Working with git and TouchDesigner isn't always an easy process, but it's often an essential part of the process of tracking your work and collaborating with others. It also encourages you to begin thinking about how to make your projects and components more modular, portable, and reuseable. Those aren't always easy practices to embrace, but they make a big difference in the amount of time you invest in future projects. It's often hard to plan for the gig in six months when you're worried about the gig on Friday - and we all have those sprints or last minute changes. 

It's also worth remember that no framework will ever be perfect - all of these things change and evolve over time, and that's the very idea behind externalizing pieces of your project's code-base. An assembly of concise individually maintainable tools is often more maintainable than [rube golbergian](https://en.wikipedia.org/wiki/Rube_Goldberg) contraption - and while it's certainly less cool, it does make it easier to make deadlines.

So, what does all this have to do with saving external tox files? TOX files are the modules of TouchDesigner - they're component operators that can be saved as individual files and dropped into any network. These custom operators are made out of other operators. In 099 they can be set to be private if you have a pro license - keeping prying eyes away from your work (if you're worried about that).

That makes these components excellent candidates for externalization, but it takes a little extra work to keep them saved and sycned. In a perfect world we would use the same saving mechanism that's employed to save our TOE file to also save any external file, or better yet, to ask us if we want to externalize a file. That, in fact, is the aim of this TOX.

### [save_for_release]()
*summary*


### [dominant_color]()
*summary*  
A tool for finding Dominant Color with openCV.

Here we find an attempt at locating dominant colors from a source image with openCV and KMeans clustering. The large idea is to sample colors from a source image build averages from clustered samples and return a best estimation of dominant color. While this works well, it's not perfect, and in this class you'll find a number of helper methods to resolve some of the shortcomings of this process. 

Procedurally, you'll find that that the process starts by saving out a small resolution version of the sampled file. This is then handed over to openCV
for some preliminary analysis before being again handed over to sklearn (sci-kit learn) for the KMeans portion of the process. While there is a built-in
function for KMeans sorting in openCV the sklearn method is a little less cumbersome and has better reference documentation for building functionality. After the clustering process each resulting sample is processed to find its luminance. Luminance values outside of the set bounds are discarded before assembling a final array of pixel values to be used. 

It's worth noting that this method relies on a number of additional python libraries. These can all be pip installed, and the recommended build approach here would be to use Python35. In the developers experience this produces the least number of errors and issues - and boy did the developer stumble along the way here.

Other considerations you'll find below are that this extension supports a multi-threaded approach to finding results. 

### [sop_to_svg]()
*summary*  

Scalable Vector Graphics (SVG) are a handy means of creating images that aren't bound by the rules of raster graphics. Illustrators and designers often use SVGs for a variety of purposes, but they're especially interesting when it comes to interacting with plotting and cutting machinery. Laser and vinyl cutters, plotters and all manner of other devices can use SVGs rather than raster based graphics.

Derivative's TouchDesigner is well known for working with raster based graphics, but there's little support for capturing and outputting SVGs as a built in approach. It does, however, support a robust python layer which is capable of handling this task. The primary design in this TouchDesigner module is to target the process of converting Surface Operators (SOPs) to SVGs so they can be plotted or laser cut.

To that end in this TOX you'll find several means of capturing and plotting your geometry.