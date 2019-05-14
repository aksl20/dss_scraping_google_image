# Scraping Google images

DSS plugin used to download images from google with a recipe into a folder managed by Dataiku.
This plugin is a dataiku wrapper of the project [google-images-download](https://github.com/hardikvasa/google-images-download).

## Recipe

Using the recipe is very straightforward. Just click on the scraping-google-image recipe in your flow and provide an output managed folder to store the images.
After the selection of your folder, you need to provide some parameter to run the scraper :
* __Keywords__: List of keywords separated by coma.
* __Number max of image__: The number of images downloaded for each keyword will not exceed this value (20 by default).
* __Filter by image format__: You can filter the result by specific image format that you need (ex: ico, svg, bmp...)
* __Color type__: Image can be downloaded as grayscale, transparent or color image.

One subfolder for each keywords will be created in the output folder. theses folders will contain all your images.
