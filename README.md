FlowChecker: a TCP Flow Analytical Framework for Network Measurements
========================================================

*Status: Stable -- Version: 1.0*

### What is FlowChecker?

FlowChecker is a Python framework for TCP flows analysis. This framework receives and processes a Comma-Separated Value (CSV) file with information collected in PCAP files. The FlowChecker framework is implemented through three main modules: The first module recognizes every flow present in the input file and produces individual CSV files containing the packet of each flow. Thus, the user defines the flows (and the associated reverse flows) to be processed in the next module; In the second module, the information regarding the Round Trip Time (RTT), jitter, Packets Per Second (PPS), throughput, and errors are recovered and aggregated; Finally, in the third module, every data from the second module summarized in informative charts created by using LaTeX/TikZ.

### Support

Contact us towards git issues requests or by the e-mail vfulber@inf.ufsm.br.

### FlowChecker Research Group

Vinícius Fülber Garcia (vfulber@inf.ufsm.br) - UFPR, Brazil <br/>
Anderson Monteiro da Rocha (amonteiro@inf.ufsm.br) - IF-Farroupilha, Brazil <br/>
Thales Nicolai Tavares (tntavares@inf.ufsm.br) - UFSM, Brazil <br/>
Nilton Camargo Batista da Silva (nbatista@inf.ufsm.br) - UFSM, Brazil <br/>
Leonardo da Cruz Marcuzzo (lmarcuzzo@inf.ufsm.br) - UFSM, Brazil

### Publications

Garcia, V. F.; Rocha, A. M.; Tavares, T. N.; Silva, N. C. B.; Marcuzzo, L. d. C.. FlowChecker: A TCP Flow Analytical Framework for Network Measurements. Encontro Anual de Tecnologia da Informação (EATI). 2017.<br/>
Rocha, A. M.; Garcia, V. F.; Tavares, T. N.; Silva, N. C. B.; Marcuzzo, L. d. C.; Lucca, L. P.; Santana, B. S.; Santos, C. R. P. d.. Flow-Checker: Um Framework Para Análise de Fluxos Utilizando Arquivos PCAP. Jornada Acadêmica Integrada (JAI). 2017.