# README

《Complementing Arm CCA with GPU》

- CAGE通过引入一个“影子任务机制”来管理保密GPU任务，从而确保GPU任务在CCA的“领域”架构下能够灵活执行，同时利用Arm CCA的内存隔离机制保护数据的机密性和完整性

- **影子任务机制**：该机制允许GPU软件堆栈创建和管理“影子GPU任务”，这些任务与实际的GPU任务相对应，但不会包含敏感数据。CAGE在实际执行任务之前，通过安全检查，将影子任务替换为真正的任务数据，以确保数据的安全性。
- **双向隔离机制**：CAGE利用Arm CCA的内存隔离机制，不仅保护CPU的内存访问，还对GPU和其他不可信外围设备进行隔离，确保它们无法访问保密数据。
- **内存保护机制的优化**：为了减小性能开销，CAGE对内存管理中的一些操作进行了优化，尤其是在GPU任务的内存访问和同步方面。

> COMPASS

-------------------------------------------

《Federated Backdoor Detection in Federated Learning》

- 联邦学习系统易受所谓的后门攻击（Backdoor Attacks），这些攻击由恶意客户端发起，目的是在模型中植入特定的行为，以便在输入特定触发器时改变模型输出。
- CrowdGuard提出了一种新颖的后门检测机制，利用客户端的反馈并分析模型隐藏层中的神经元行为。具体方法包括：
  - **隐层后门检测指标（HLBIM）**
  - **迭代修剪机制**
  - **客户端反馈循环**

- CrowdGuard通过以下方法保障隐私：
  - **可信执行环境（TEEs）**：CrowdGuard利用TEEs在客户端和服务器上执行敏感代码，确保模型的机密性，即使服务器被攻破，恶意方也无法访问客户端的本地模型。
  - **反馈保护**：CrowdGuard通过分层聚类算法来汇总来自客户端的反馈，防止恶意客户端提供错误反馈，扰乱后门检测。

> 主要学习TEEs部分是怎么应用的

-------------------------------

《Hybrid Trust Multi-party Computation with Trusted Execution Environment》

- 探讨了一种混合信任的多方计算（MPC）框架，结合了硬件安全机制，如可信执行环境（Trusted Execution Environment，TEE），特别是**Intel SGX**，以应对不同参与方对TEE信任程度不一的场景。
- 多方计算（MPC）允许多个参与方在不暴露各自敏感数据的情况下，共同计算某个函数的输出。

- 传统的MPC协议依赖大量的加密计算，效率较低，尤其是在处理大规模数据集时。Intel的SGX等可信执行环境（TEE）提供了硬件隔离机制，能在较少加密开销的情况下保护计算数据的安全，从而成为一种替代方案。
- 尽管TEE能显著提高效率，依然存在一些安全隐患，特别是各种侧信道攻击，使得不同的参与方对TEE的信任程度各不相同。
- 作者提出了**HYBRTC**（Hybrid Trust Computation）框架，这是一个适用于混合信任环境的通用框架。该框架**允许不同的参与方根据他们对TEE的信任程度选择相应的计算模式**，从而在确保隐私的前提下，充分利用TEE和传统的MPC协议的优势。

- HYBRTC在设计中面临以下挑战：
  - **协议划分**：如何合理划分TEE与MPC的任务，避免敏感数据在不同计算模式间切换时泄露。例如，某些中间结果可能包含敏感信息，不能简单地在MPC和TEE之间传递。
  - **安全性要求**：由于每个参与方对TEE的信任程度不同，需要根据不同的安全需求灵活调整计算方式，确保各参与方的数据隐私不被泄露。
  - **形式化安全模型**：为确保混合信任计算的安全性，作者提出了一种新的多面可信硬件模型（FTH），该模型形式化了TEE的行为，并在理论上证明了框架的安全性

- 为了验证HYBRTC的有效性，作者在Intel SGX环境中实现了该框架，并进行了一系列实验。实验结果表明，与传统的纯MPC方案相比，HYBRTC在确保安全的前提下显著提高了计算效率。例如，在分布式查询场景下，HYBRTC在两个拥有220条记录的服务器上执行选择-连接查询，仅耗时165.82秒，性能比纯加密方案提升了18,752倍。

> 学习怎么结合MPC

--------------------------

《Novel Bus Fault Attack to Break ARM TrustZone》

- 讨论了一种新的总线故障攻击（Bus Fault Attack），旨在破坏ARM TrustZone的安全性，研究发现，尽管ARM TrustZone能有效应对大多数传统攻击，但总线故障攻击却能绕过其防御机制。
- 总线故障攻击是指通过电磁脉冲（EM）等手段在处理器与内存交互时对系统总线施加故障。攻击者可以在存储或加载指令执行时注入故障，导致数据或地址被篡改，从而危害安全执行环境。
- 总线故障攻击的主要贡献
  - **数据总线故障攻击**：通过对数据总线的故障注入，可以破坏AES（高级加密标准）S盒的查表实现，进而发起差分故障分析（DFA）攻击，恢复加密密钥。
  - **地址总线故障攻击**：利用地址总线上的故障，攻击者可以修改内存地址，导致内存访问冲突，进而泄露后量子加密算法（例如Dilithium和SABER）的密钥。
  - **ARM TrustZone攻击**：本文展示了如何通过总线故障攻击，绕过ARM TrustZone的签名验证步骤，安装恶意的可信应用（Trusted Applications, TAs）。这类攻击不仅危害TrustZone，还能泄露其它可信应用的对称加密密钥，导致系统的整体安全性崩溃。
- 为了应对这些新型总线故障攻击，作者提出了一些可能的防御措施，包括加强总线的保护和改进硬件设计。然而，这些防御措施需要额外的硬件支持，当前的ARM TrustZone实现尚未全面应对这类攻击。

> 这篇与trustzone相关，提出了一种可行的攻击方案，但是还未提出解决方案，可以作为以后的一个项目思路，目前优先度不高

---------------

《Scalable Leakage-Free Cache Hierarchies for Trusted Execution Environments (TEEs)》- 

- 在现代计算机系统中，**缓存层次结构成为许多侧信道攻击的目标**，这些攻击通过观察缓存中的内存访问模式来推测敏感信息，甚至会威胁到利用可信执行环境（TEE）保护的应用程序。
- 尽管TEE在逻辑上隔离了执行环境，硬件资源的物理共享（特别是缓存）仍然使其容易受到攻击。
- 目标是设计一个安全的缓存层次结构，以**防止攻击者通过缓存侧信道获取隐私数据**。

- **TEE-SHirT**（Secure Hierarchies for TEEs）框架通过对多级缓存进行分区和管理，实现了对缓存侧信道攻击的有效防御。它的设计包括：
  - **分区的共享LLC（Last-Level Cache）**：LLC是系统中缓存层次结构的最后一级缓存，由多个处理器核心共享。TEE-SHirT通过将LLC进行分区，使得不同的应用程序（包括运行在TEE中的应用程序）使用不同的缓存分区，从而防止它们之间的信息泄露。
  - **分区的私有L2缓存**：除了LLC，L2缓存也需要进行分区。传统的缓存一致性协议假设在每个缓存中只能存在一个缓存行副本，但TEE-SHirT设计了一种新的机制来保持缓存数据的一致性。
  - **L1缓存刷新**：L1缓存不进行分区，但在上下文切换时被刷新，以防止缓存中的数据被不安全的上下文访问。
- TEE-SHirT在设计中面临多个技术挑战，本文提出了创新性的解决方案：
  1. **缓存分区元数据的虚拟化**：为了解决缓存分区元数据数量有限的问题，TEE-SHirT将分区元数据虚拟化，并集成到Intel SGX中。这种虚拟化允许在上下文切换时保存和恢复缓存分区信息，从而避免每次切换时都清空缓存分区，提升了性能。
  2. **一致性与缓存一致性问题**：在多线程执行的情况下，多个线程可能会同时访问同一块数据。TEE-SHirT通过在不同缓存层级之间同步分区元数据来解决这个问题，确保多线程之间的数据共享和一致性。
  3. **安全性模型**：TEE-SHirT通过形式化安全分析，建立了一个缓存感知和TEE感知的操作语义模型，证明了设计的安全性。该模型涵盖了从缓存分配、上下文切换到缓存一致性的所有操作，确保了系统的抗侧信道攻击能力。

> TEE侧信道攻击的防御措施，主要与缓存相关，目前的优先度不高

-----------------

《Testing and Repairing MPC-Hardened Deep Learning Models》

- MPC协议的复杂性以及为了兼容深度学习模型而进行的各种优化（例如定点数表示、非线性函数的近似）可能会导致模型在推理阶段产生不准确的预测
- 为了检测这些由于MPC转换而导致的模型输出偏差，作者提出了**MPCDIFF**，这是第一个专门用于测试和修复MPC保护的深度学习模型的工具。该工具通过差分测试法发现导致MPC保护模型输出偏差的输入，然后定位出引发误差的计算单元，并自动修复这些缺陷，从而提高模型的鲁棒性。

> MPC相关的技术，暂时优先度不高

-----------------------------