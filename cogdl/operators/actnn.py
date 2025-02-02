import os
import torch
import torch.nn as nn
from torch.utils.cpp_extension import load

path = os.path.join(os.path.dirname(__file__))

try:
    qdropout = load(
        name="qdropout",
        sources=[os.path.join(path, "actnn/actnn.cc"), os.path.join(path, "actnn/actnn.cu")],
        verbose=False,
    )

except Exception:
    print("Please install actnn library first.")
    qdropout = None


class QDropout(nn.Module):
    def __init__(self, p=0.5):
        super().__init__()
        self.p = p

    def forward(self, input: torch.Tensor) -> torch.Tensor:
        return qdropout.act_quantized_dropout(input, self.p)
