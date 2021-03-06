![alt text](streamlit_app/assets/app_logo_yugi.jpg)
# BakuGAN -> YugiGAN

- Initally I planned to generate anime characters (BakuGAN), but given the lack of harmony in the structure of images I got from web scraping, it didn't seem like a GAN could learn the generative process behind such disparate images
- So I pivoted to Yugioh card generation with **YugiGAN**, as I will always be a nostalgic fan of Yugioh cards & the animes (DM, GX and 5D's, didn't watch the rest)!
- The model is trained on a dataset of 10K+ images. You can see the hyperparameters I chose in the script. So far it looks like this:
![alt text](data/processed/finalized_figures/Figure_6.png)

Built with ❤️ by [emiledesmaili](https://github.com/emiledesmaili)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/emiledesmaili/bakugan)

## What's this?

- `README.md`: This Document! To help you find your way around
- `streamlit_app.py`: The main app that gets run by [`streamlit`](https://docs.streamlit.io/)
- `requirements.txt`: Pins the version of packages needed
- `LICENSE`: Follows Streamlit's use of Apache 2.0 Open Source License
- `.gitignore`: Tells git to avoid comitting / scanning certain local-specific files
- `.streamlit/config.toml`: Customizes the behaviour of streamlit without specifying command line arguments (`streamlit config show`)
- `Makefile`: Provides useful commands for working on the project such as `run`, `lint`, `test`, and `test-e2e`
- `requirements.dev.txt`: Provides packages useful for development but not necessarily production deployment. Also includes all of `requirements.txt` via `-r`
- `pyproject.toml`: Provides a main configuration point for Python dev tools
- `.flake8`: Because `flake8` doesn't play nicely with `pyproject.toml` out of the box
- `.pre-commit-config.yaml`: Provides safeguards for what you commit and push to your repo
- `tests/`: Folder for tests to be picked up by `pytest`
- `app.json`: Provides "Deploy to Heroku" functionality / specification
- `Procfile`: Special file to tell Heroku how to run our app (`streamlit run`) (see [docs](https://devcenter.heroku.com/articles/procfile))
- `runtime.txt`: Special file to tell Heroku which python version to use (see [supported runtimes](https://devcenter.heroku.com/articles/python-support#supported-runtimes))

## Local Setup

Assumes working python installation and some command line knowledge ([install python with conda guide](https://tech.gerardbentley.com/python/beginner/2022/01/29/install-python.html)).

```sh
# External users: download Files
git clone git@github.com:emiledesmaili/bakugan.git

# Go to correct directory
cd bakugan

# For the anime pic scraper, run the streamlit app (will install dependencies in a virtualenvironment in the folder venv)
make run

# for YugiGAN: 
run models.py
```
Open your browser to [http://localhost:8501/](http://localhost:8501/) if it doesn't open automatically.

### Local Development

The `Makefile` and development requirements provide some handy Python tools for writing better code.
See the `Makefile` for more detail

```sh
# Run black, isort, and flake8 on your codebase
make lint
# Run pytest with coverage report on all tests not marked with `@pytest.mark.e2e`
make test
# Run pytest on tests marked e2e (NOTE: e2e tests require `make run` to be running in a separate terminal)
make test-e2e
# Run pytest on tests marked e2e and replace visual baseline images
make test-e2e-baseline
# After running tests, display the coverage html report on localhost
make coverage
```
## Deploy

For the easiest experience, deploy to [Streamlit Cloud](https://streamlit.io/cloud)

For other options, see [Streamilt deployment wiki](https://discuss.streamlit.io/t/streamlit-deployment-guide-wiki/5099)

## Credits

This package was created with Cookiecutter and the `gerardrbentley/cookiecutter-streamlit` project template.

- Cookiecutter: [https://github.com/audreyr/cookiecutter](https://github.com/audreyr/cookiecutter)
- `gerardrbentley/cookiecutter-streamlit`: [https://github.com/gerardrbentley/cookiecutter-streamlit](https://github.com/gerardrbentley/cookiecutter-streamlit)
