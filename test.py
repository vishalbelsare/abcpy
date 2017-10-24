from abcpy import ProbabilisticModel as pb; 
a = pb.Uniform([[0,0],[5,10]])
b = pb.Uniform([[10],[20]])
c = pb.Uniform([[a], [b, 5]])
d = pb.Uniform([[c], [c]])
print(d.sample_from_distribution(25))
