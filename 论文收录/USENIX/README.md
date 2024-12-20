# README

《Defending Against Data Reconstruction Attacks in Federated Learning: An Information Theory Approach》

- 联邦学习在不同客户端之间传递模型参数以避免直接共享数据，旨在通过这种方式减少隐私泄露的风险。尽管如此，研究表明，通过分析这些传递的参数，攻击者仍然能够发起**数据重建攻击（DRA）**。

> 这篇跟攻防有关，且攻击难度较高，文章优先级较低

------------------

《Hijacking Attacks Against Neural Networks》

- 论文提出了一种新的劫持攻击方法，称为**CleanSheet**。该方法能够在无需篡改训练过程的情况下，通过分析模型的训练数据实现高效的攻击。
- 主要原理是利用神经网络对“鲁棒特征”的敏感性，构造触发器（trigger），通过向任意输入添加触发器误导模型输出错误结果。
- CleanSheet与传统的后门攻击类似，但它不需要攻击者参与模型的训练，只需了解一部分训练数据即可。

> 这篇也是与攻防有关，文章优先度较低

----------------------------

《Lotto: Secure Participant Selection Against Adversarial Servers in Federated Learning》

- 在现有的技术中，联邦学习系统**假设多数参与者是诚实**的。
- 论文提出了联邦学习中的一个新问题：即**服务器可能恶意选择参与者**，导致不诚实的客户端占据多数，从而破坏系统的隐私保障。
- 论文提出了一个名为Lotto的框架，旨在解决这一问题。
- Lotto主要通过两种算法（随机选择和知情选择）来保障参与者的安全选择。
  1. **随机选择**：Lotto允许每个**客户端**使用可验证的随机数函数（VRF），**独立地决定自己是否参与联邦学习**。在这种模式下，客户端通过自己计算出的随机数决定是否参加，而不是由服务器决定。
  2. **知情选择**：在一些情况下，联邦学习系统会根据客户端的性能和数据质量来选择参与者。这种选择方式称为知情选择。Lotto通过在精细化后的客户端池中进行随机选择来近似这种算法，以减少服务器操纵参与者选择的风险。

> 我们的目的目前是搭建隐私计算平台，那么假定服务器就是可信任的。文章目前的优先度较低

---------------------