## Dataset

We are using the dataset provided by Enyan Dai in 
[FakeHealth](https://github.com/EnyanDai/FakeHealth), which contains 
health articles rated from 0 (mostly or totally fake) to 5 (mostly or 
totally true). The dataset was originally crafted to supplement the paper 
[Ginger Cannot Cure Cancer: Battling Fake Health News with a Comprehensive 
Data Repository](https://arxiv.org/abs/2002.00837) by Dai, Sun and Wang (2020). 
Additionally, it was also used by Kumari et al. (2021) in the paper [Debunking 
health fake news with domain specific pre-trained 
model](https://www.sciencedirect.com/science/article/pii/S2666285X21000662).

You can download the original dataset [here](https://github.com/EnyanDai/FakeHealth).


### Processing 

The original dataset is not in CSV format and has many fields we are not 
currently intereted in. We've extracted the following fields of interest and
turned it into a single `.csv` file (which is not included in this repository):

If you want to generate that same `dataset.csv` file, you can do so runing 
[generate_ds.py](generate_ds.py) in [FakeHealth](https://github.com/EnyanDai/FakeHealth)
root.


