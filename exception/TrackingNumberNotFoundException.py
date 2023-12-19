class TrackingNumberNotFoundException(Exception):
    def __init__(self, tracking_number):
        super().__init__(f"Tracking Number: {tracking_number} not found in the system.")
