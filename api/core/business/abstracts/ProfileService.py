from profiles.models import Profile
from profiles.repository.ProfilesRepository import ProfileRepository

class ProfileService:
    def __init__(self, profileRepository):
        self.profileRepository = profileRepository

    def saveProfile(self, profile):
        pass

    def updateProfile(self, profile, profile_id):
        pass

    def deleteProfile(self, profile_id):
        pass

profileService = ProfileService(ProfileRepository(Profile()))

