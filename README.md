<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** See the bottom of this document for the declaration of the reference variables
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- Title -->
<h3 align="center">Machine Learning Algoirhtms on Medical Data</h3>

  <p align="center">
    <br />
    <a href="https://github.com/seanpden/oopTest/issues">Report Bug</a>
    ·
    <a href="https://github.com/seanpden/oopTest/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This repository houses my testing of machine learning and data mining algorithms to diagnose acute myloid leukemia. In the 'datainterface' class I've implemented a few algorithms that I'm most keen on testing. I have a lot of plans in the future for expansion - you can see those in the roadmap section.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [SciKit-Learn](https://scikit-learn.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

You must have the most recent python version installed. This project relies on scikit-learn for some of its calculations.
* scikit-learn
  ```sh
  pip install -U scikit-learn
  ```

### Installation

1. You can simply download the repository OR
2. Clone the repo
   ```sh
   git clone https://github.com/seanpden/oopTest.git
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This project is meant to be expanded on and acts as a basis for my paper on effectiveness of machine learning and data mining algorithms in the medical field. 

I operate using the driver.py file. This is where I import and stage my dataset. I also execute my tests here. 

As more updates occur, the datainterface file will be more broad and the usage more general. For now, you can import an altered cytometry data sheet that includes specific features and labels. Once that data is imported, you can perform various operations on it such as:
* Gaussian Naive Bayes algorithm
* Random Forest algorithm
* Decision Tree algorithm
* etc...

_For my personal usage, please refer to my [driver file](https://github.com/seanpden/oopTest/driver.py)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [X] Create skeleton for modular implementation
- [ ] Generalize data splitting
- [ ] Add more algorithms
- [ ] Interface with 'person' objects instead of dataset as a whole

See the [changelog](https://github.com/seanpden/oopTest/CHANGELOG.md) for a full list of completed features.

See the [open issues](https://github.com/seanpden/oopTest/issues) for proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. I aim to comple this on my own, but I would love to hear from anyone about features that would improve or compliment my goal of proving the utility of these algorithms in a medical environment.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Sean Denney - [seanpden](https://www.linkedin.com/in/seanpden/) - [seanden522@gmail.com](seanden522@gmail.com)

Project Link: [https://github.com/seanpden/oopTest](https://github.com/seanpden/oopTest)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [README template](https://github.com/othneildrew/Best-README-Template)
* [All of the scikit docs lol](https://scikit-learn.org/stable/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[issues-shield]: https://img.shields.io/github/issues/seanpden/oopTest.svg?style=for-the-badge

[issues-url]: https://github.com/seanpden/oopTest/issues

[license-shield]: https://img.shields.io/github/license/seanpden/oopTest.svg?style=for-the-badge

[license-url]: https://github.com/seanpden/oopTest/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/seanpden