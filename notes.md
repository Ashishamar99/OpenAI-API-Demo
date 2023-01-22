#### Notes

Parameters for request are :
![requestparams.png](images/request%20params%20for%20text%20completion.png)

<hr />

- max_tokens - The maximum number of tokens to generate in the completion.
![tokens.png](images/tokens.png)
- temperature - temperature is like a value for the model based on which it will decide whether if it needs to be creative or not. - [article link](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277)
- top_p - of the generated tokens will filter and give according to top probability value.
![top_p.png](images/topp.png)
- n - is the number of completions to generate for each prompt.