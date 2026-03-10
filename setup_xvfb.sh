#!/bin/bash

# Update package lists and install Xvfb
sudo apt-get update
sudo apt-get install -y xvfb

# Create the systemd service file for Xvfb
sudo bash -c 'cat > /etc/systemd/system/xvfb.service <<EOF
[Unit]
Description=X Virtual Framebuffer Service
After=network.target

[Service]
ExecStart=/usr/bin/Xvfb :99 -screen 0 1024x768x24
Restart=always
User=nobody
Environment=DISPLAY=:99

[Install]
WantedBy=multi-user.target
EOF'

# Reload systemd to apply the new service
sudo systemctl daemon-reload

# Enable and start the Xvfb service
sudo systemctl enable xvfb
sudo systemctl start xvfb

# Add DISPLAY variable to the user's shell configuration file
if [ -f ~/.zshrc ]; then
    if ! grep -q "export DISPLAY=:99" ~/.zshrc; then
        echo "export DISPLAY=:99" >> ~/.zshrc
    fi
fi

# Apply the changes to the current session
export DISPLAY=:99
source ~/.zshrc

echo "Xvfb setup complete. DISPLAY variable set to :99."
