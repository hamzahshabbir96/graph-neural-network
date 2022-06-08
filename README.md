
# Graph Neural Network for prediction of critical temperature of superconductor

Despite of good performance of compositional model, one of the major limitations is lacked to conserving structural features. Since structure of crystal has significant impact on superconductivity, approach should be to consider structural features into account. Structure of a molecules naturally can be represented as a graph with elements being node and bonds between elements being edge or arc. In machine learning, mostly structural data are dominant where we have fixed input length. But in real life we might not have always structured data such as in case of superconductor. Although there are ways to convert unstructured data to structured data, a lot of information is lost, which might be crucial and have great impact on model. One of the promising approaches of training model along with structural feature is Graph neural networks.

![Image](pictures/mainpic.png)

## Classes and Functions
### GraphNeuralSuperconductor
GraphNeuralSuperconductor is the main class that contains computation and weight initialization. This can be initialized by following command and requires number of features of nodes as input

```bash

        adj, number_of_nodes, critical_temperature_,features = trainset.nextbatch(batchsize)
        s,_ = net.forward_propagation(number_of_nodes,adj,features)  
        loss = net.loss(s,critical_temperature_)
        net.backward_propagation(loss,critical_temperature_,upsilon)
```
### Preprocess data
Since we have dataset in the text format in specific format. To make it available for computation, a class has been built which requires path of dataset as input and output train and test dataset, that can further be used.
```bash
  from utils import preprocessdata
  path="datasets/train"
  trainset,testset = preprocessdata.Preprocess(path).get_data()
```

### Extraction of adjacent matrix, critical temperature, features and number of nodes
Following method of class can be used to extract data information such as adjacent matrix, critical temperature, features and number of nodes
```bash

   adjacent_matrix, number_of_nodes, critical_temperature_,features = trainset.next_dataset(batchsize)
        
```

### Forward propagation
Following method can be used for 







- [@hamzahshabbir](https://www.github.com/octokatherine)

## Authors

- [@hamzahshabbir](https://www.github.com/octokatherine)

  
## Acknowledgements

 - [Awesome Readme Templates](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Awesome README](https://github.com/matiassingers/awesome-readme)
 - [How to write a Good readme](https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project)

  
## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)

  
## Feedback

If you have any feedback, please reach out to us at fake@fake.com

  
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://katherinempeterson.com/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/)

  
## FAQ

#### Question 1

Answer 1

#### Question 2

Answer 2

  
## Installation

Install my-project with npm

```bash
  npm install my-project
  cd my-project
```
    
## 🚀 About Me
I'm a full stack developer...

  
## Documentation

[Documentation](https://linktodocumentation)

  
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`

  
