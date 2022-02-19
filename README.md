## fake-plugin-starter
A fake kedro plugin to test starter injection functionnality

## How to use

Setup the my development kedro version and install the plugin

```bash
conda create -n fps python=3.8 -y
conda activate fps
pip install git+https://github.com/Galileo-Galilei/kedro.git@plugins-starters
pip install git+https://github.com/Galileo-Galilei/fake-plugin-starter.git
kedro starter list
```

You should see: 

```bash
(*) my_fake_starter: http://google.com # my extra starter
astro-airflow-iris: https://github.com/kedro-org/kedro-starters/tree/main/astro-airflow-iris
astro-iris: https://github.com/kedro-org/kedro-starters/tree/main/astro-airflow-iris
mini-kedro: https://github.com/kedro-org/kedro-starters/tree/main/mini-kedro
pandas-iris: https://github.com/kedro-org/kedro-starters/tree/main/pandas-iris
pyspark: https://github.com/kedro-org/kedro-starters/tree/main/pyspark
pyspark-iris: https://github.com/kedro-org/kedro-starters/tree/main/pyspark-iris
spaceflights: https://github.com/kedro-org/kedro-starters/tree/main/spaceflights
```