import torch.nn as nn


class ConvAutoEncoder(nn.Module):
    def __init__(self, pretrained_model):
        super().__init__()
        self.encoder = nn.Sequential(*list(pretrained_model.children())[:2])
        self.compressor = nn.Sequential(
            nn.Conv2d(in_channels=32, out_channels=4,
                      kernel_size=3, padding=1),
            nn.BatchNorm2d(num_features=4),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Conv2d(in_channels=4, out_channels=32,
                      kernel_size=3, padding=1),
            nn.BatchNorm2d(num_features=32),
            nn.ReLU(),
            nn.Upsample(scale_factor=2, mode='nearest'),
            nn.Conv2d(in_channels=32, out_channels=16,
                      kernel_size=5, padding=2),
            nn.BatchNorm2d(num_features=16),
            nn.ReLU(),
            nn.Upsample(scale_factor=2, mode='nearest'),
            nn.Conv2d(in_channels=16, out_channels=1,
                      kernel_size=5, padding=2),
            nn.BatchNorm2d(num_features=1),
            nn.Sigmoid()
        )

    def forward(self, t):
        t = self.encoder(t)
        t = self.compressor(t)
        t = self.decoder(t)

        return t
