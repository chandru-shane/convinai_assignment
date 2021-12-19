
USER_FIELDS = {
    'Id': 'salesforce_id',
    'Username': 'username',
    'Email': 'email',
    'FirstName': 'firstname',
    'LastName': 'lastname',
    'Name':'name',
    'Phone':'phone',
    'MobilePhone': 'mobile',
    'CompanyName': 'company_name',
    'Address':'address'
    }
    
ACCOUNT_FIELDS = {
    'Id': 'salesforce_id',
    'AnnualRevenue': 'annual_revenue',
    'Name': 'name',
    'AccountNumber': 'account_number',
    'Website': 'website',
    'BillingAddress':'billing_address',
    'ShippingAddress':'shipping_address'
}

CONTACT_FIELDS = {
    'Id': 'salesforce_id',
    'FirstName': 'firstname',
    'LastName': 'lastname',
    'Name': 'name',
    'AccountId': 'account_id',
    'Phone': 'phone',
    'Email': 'email',
    'MobilePhone': 'mobile_phone',
    'MailingAddress': 'mailing_address' 
}



"""
RESPONSE SCHEMA FROM SALESFORCE

ACCOUNTS
[  { attributes: {'type': 'Account', 'url': '/services/data/v45.0/sobjects/Account/0015j00000DzvF0AAJ'} }  
  { Id: 0015j00000DzvF0AAJ }  
  { IsDeleted: False }  
  { MasterRecordId: None }  
  { Name: Dickenson plc }  
  { Type: Customer - Channel }  
  { ParentId: None }  
  { BillingStreet: 1301 Hoch Drive }  
  { BillingCity: Lawrence }  
  { BillingState: KS }  
  { BillingPostalCode: 66045 }  
  { BillingCountry: USA }  
  { BillingLatitude: None }  
  { BillingLongitude: None }  
  { BillingGeocodeAccuracy: None }  
  { BillingAddress: {'city': 'Lawrence', 'country': 'USA', 'geocodeAccuracy': None, 'latitude': None, 'longitude': None, 'postalCode': '66045', 'state': 'KS', 'street': '1301 Hoch Drive'} }  
  { ShippingStreet: 1301 Hoch Drive }  
  { ShippingCity: Lawrence }  
  { ShippingState: KS }  
  { ShippingPostalCode: 66045 }  
  { ShippingCountry: USA }  
  { ShippingLatitude: None }  
  { ShippingLongitude: None }  
  { ShippingGeocodeAccuracy: None }  
  { ShippingAddress: {'city': 'Lawrence', 'country': 'USA', 'geocodeAccuracy': None, 'latitude': None, 'longitude': None, 'postalCode': '66045', 'state': 'KS', 'street': '1301 Hoch Drive'} }  
  { Phone: (785) 241-6200 }  
  { Fax: (785) 241-6201 }  
  { AccountNumber: CC634267 }  
  { Website: dickenson-consulting.com }  
  { PhotoUrl: /services/images/photo/0015j00000DzvF0AAJ }  
  { Sic: 6752 }  
  { Industry: Consulting }  
  { AnnualRevenue: 50000000.0 }  
  { NumberOfEmployees: 120 }  
  { Ownership: Private }  
  { TickerSymbol: None }  
  { Description: None }  
  { Rating: None }  
  { Site: None }  
  { OwnerId: 0055j000002oWyfAAE }  
  { CreatedDate: 2021-12-17T13:50:14.000+0000 }  
  { CreatedById: 0055j000002oWyfAAE }  
  { LastModifiedDate: 2021-12-17T13:50:14.000+0000 }  
  { LastModifiedById: 0055j000002oWyfAAE }  
  { SystemModstamp: 2021-12-17T13:50:14.000+0000 }  
  { LastActivityDate: None }  
  { LastViewedDate: 2021-12-18T15:24:58.000+0000 }  
  { LastReferencedDate: 2021-12-18T15:24:58.000+0000 }  
  { Jigsaw: None }  
  { JigsawCompanyId: None }  
  { CleanStatus: Pending }  
  { AccountSource: None }  
  { DunsNumber: None }  
  { Tradestyle: None }  
  { NaicsCode: None }  
  { NaicsDesc: None }  
  { YearStarted: None }  
  { SicDesc: None }  
  { DandbCompanyId: None }  
  { OperatingHoursId: None }  
  { CustomerPriority__c: Low }  
  { SLA__c: Bronze }  
  { Active__c: Yes }  
  { NumberofLocations__c: 2.0 }  
  { UpsellOpportunity__c: No }  
  { SLASerialNumber__c: 7425 }  
  { SLAExpirationDate__c: 2022-07-14 }  
]

USERS

[  { attributes: {'type': 'User', 'url': '/services/data/v45.0/sobjects/User/0055j0000032QsPAAU'} }  
  { Id: 0055j0000032QsPAAU }  
  { Username: insightssecurity@00d5j000003hlaceau.com }  
  { LastName: User }  
  { FirstName: Security }  
  { Name: Security User }  
  { CompanyName: New Company Name }  
  { Division: None }  
  { Department: None }  
  { Title: None }  
  { Street: None }  
  { City: None }  
  { State: None }  
  { PostalCode: None }  
  { Country: xx }  
  { Latitude: None }  
  { Longitude: None }  
  { GeocodeAccuracy: None }  
  { Address: {'city': None, 'country': 'xx', 'geocodeAccuracy': None, 'latitude': None, 'longitude': None, 'postalCode': None, 'state': None, 'street': None} }  
  { Email: insightssecurity@example.com }  
  { EmailPreferencesAutoBcc: True }  
  { EmailPreferencesAutoBccStayInTouch: False }  
  { EmailPreferencesStayInTouchReminder: True }  
  { SenderEmail: None }  
  { SenderName: None }  
  { Signature: None }  
  { StayInTouchSubject: None }  
  { StayInTouchSignature: None }  
  { StayInTouchNote: None }  
  { Phone: None }  
  { Fax: None }  
  { MobilePhone: None }  
  { Alias: sec }  
  { CommunityNickname: insightssecurity1.4407085845464958E12 }  
  { BadgeText:  }  
  { IsActive: True }  
  { TimeZoneSidKey: America/Los_Angeles }  
  { UserRoleId: None }  
  { LocaleSidKey: en_US }  
  { ReceivesInfoEmails: True }  
  { ReceivesAdminInfoEmails: False }  
  { EmailEncodingKey: UTF-8 }  
  { ProfileId: 00e5j000002ButcAAC }  
  { UserType: Standard }  
  { LanguageLocaleKey: en_US }  
  { EmployeeNumber: None }  
  { DelegatedApproverId: None }  
  { ManagerId: None }  
  { LastLoginDate: None }  
  { LastPasswordChangeDate: None }  
  { CreatedDate: 2021-12-17T13:50:14.000+0000 }  
  { CreatedById: 0055j000002oWyfAAE }  
  { LastModifiedDate: 2021-12-17T13:50:14.000+0000 }  
  { LastModifiedById: 0055j000002oWyfAAE }  
  { SystemModstamp: 2021-12-17T14:06:25.000+0000 }  
  { OfflineTrialExpirationDate: None }  
  { OfflinePdaTrialExpirationDate: None }  
  { UserPermissionsMarketingUser: False }  
  { UserPermissionsOfflineUser: False }  
  { UserPermissionsCallCenterAutoLogin: False }  
  { UserPermissionsMobileUser: False }  
  { UserPermissionsSFContentUser: False }  
  { UserPermissionsKnowledgeUser: False }  
  { UserPermissionsInteractionUser: False }  
  { UserPermissionsSupportUser: False }  
  { UserPermissionsJigsawProspectingUser: False }  
  { UserPermissionsSiteforceContributorUser: False }  
  { UserPermissionsSiteforcePublisherUser: False }  
  { UserPermissionsWorkDotComUserFeature: False }  
  { ForecastEnabled: False }  
  { UserPreferencesActivityRemindersPopup: True }  
  { UserPreferencesEventRemindersCheckboxDefault: True }  
  { UserPreferencesTaskRemindersCheckboxDefault: True }  
  { UserPreferencesReminderSoundOff: False }  
  { UserPreferencesDisableAllFeedsEmail: False }  
  { UserPreferencesDisableFollowersEmail: False }  
  { UserPreferencesDisableProfilePostEmail: False }  
  { UserPreferencesDisableChangeCommentEmail: False }  
  { UserPreferencesDisableLaterCommentEmail: False }  
  { UserPreferencesDisProfPostCommentEmail: False }  
  { UserPreferencesContentNoEmail: False }  
  { UserPreferencesContentEmailAsAndWhen: False }  
  { UserPreferencesApexPagesDeveloperMode: False }  
  { UserPreferencesHideCSNGetChatterMobileTask: False }  
  { UserPreferencesDisableMentionsPostEmail: False }  
  { UserPreferencesDisMentionsCommentEmail: False }  
  { UserPreferencesHideCSNDesktopTask: False }  
  { UserPreferencesHideChatterOnboardingSplash: False }  
  { UserPreferencesHideSecondChatterOnboardingSplash: False }  
  { UserPreferencesDisCommentAfterLikeEmail: False }  
  { UserPreferencesDisableLikeEmail: False }  
  { UserPreferencesSortFeedByComment: False }  
  { UserPreferencesDisableMessageEmail: False }  
  { UserPreferencesJigsawListUser: False }  
  { UserPreferencesDisableBookmarkEmail: False }  
  { UserPreferencesDisableSharePostEmail: False }  
  { UserPreferencesEnableAutoSubForFeeds: False }  
  { UserPreferencesDisableFileShareNotificationsForApi: False }  
  { UserPreferencesShowTitleToExternalUsers: False }  
  { UserPreferencesShowManagerToExternalUsers: False }  
  { UserPreferencesShowEmailToExternalUsers: False }  
  { UserPreferencesShowWorkPhoneToExternalUsers: False }  
  { UserPreferencesShowMobilePhoneToExternalUsers: False }  
  { UserPreferencesShowFaxToExternalUsers: False }  
  { UserPreferencesShowStreetAddressToExternalUsers: False }  
  { UserPreferencesShowCityToExternalUsers: False }  
  { UserPreferencesShowStateToExternalUsers: False }  
  { UserPreferencesShowPostalCodeToExternalUsers: False }  
  { UserPreferencesShowCountryToExternalUsers: False }  
  { UserPreferencesShowProfilePicToGuestUsers: False }  
  { UserPreferencesShowTitleToGuestUsers: False }  
  { UserPreferencesShowCityToGuestUsers: False }  
  { UserPreferencesShowStateToGuestUsers: False }  
  { UserPreferencesShowPostalCodeToGuestUsers: False }  
  { UserPreferencesShowCountryToGuestUsers: False }  
  { UserPreferencesDisableFeedbackEmail: False }  
  { UserPreferencesDisableWorkEmail: False }  
  { UserPreferencesPipelineViewHideHelpPopover: False }  
  { UserPreferencesHideS1BrowserUI: False }  
  { UserPreferencesDisableEndorsementEmail: False }  
  { UserPreferencesPathAssistantCollapsed: False }  
  { UserPreferencesCacheDiagnostics: False }  
  { UserPreferencesShowEmailToGuestUsers: False }  
  { UserPreferencesShowManagerToGuestUsers: False }  
  { UserPreferencesShowWorkPhoneToGuestUsers: False }  
  { UserPreferencesShowMobilePhoneToGuestUsers: False }  
  { UserPreferencesShowFaxToGuestUsers: False }  
  { UserPreferencesShowStreetAddressToGuestUsers: False }  
  { UserPreferencesLightningExperiencePreferred: True }  
  { UserPreferencesPreviewLightning: False }  
  { UserPreferencesHideEndUserOnboardingAssistantModal: False }  
  { UserPreferencesHideLightningMigrationModal: False }  
  { UserPreferencesHideSfxWelcomeMat: False }  
  { UserPreferencesHideBiggerPhotoCallout: False }  
  { UserPreferencesGlobalNavBarWTShown: False }  
  { UserPreferencesGlobalNavGridMenuWTShown: False }  
  { UserPreferencesCreateLEXAppsWTShown: False }  
  { UserPreferencesFavoritesWTShown: False }  
  { UserPreferencesRecordHomeSectionCollapseWTShown: False }  
  { UserPreferencesRecordHomeReservedWTShown: False }  
  { UserPreferencesFavoritesShowTopFavorites: False }  
  { UserPreferencesExcludeMailAppAttachments: False }  
  { UserPreferencesSuppressTaskSFXReminders: False }  
  { UserPreferencesSuppressEventSFXReminders: False }  
  { UserPreferencesPreviewCustomTheme: False }  
  { UserPreferencesHasCelebrationBadge: False }  
  { UserPreferencesUserDebugModePref: False }  
  { UserPreferencesNewLightningReportRunPageEnabled: False }  
  { ContactId: None }  
  { AccountId: None }  
  { CallCenterId: None }  
  { Extension: None }  
  { FederationIdentifier: None }  
  { AboutMe: None }  
  { FullPhotoUrl: https://yourcompany63-dev-ed--c.documentforce.com/profilephoto/005/F }  
  { SmallPhotoUrl: https://yourcompany63-dev-ed--c.documentforce.com/profilephoto/005/T }  
  { IsExtIndicatorVisible: False }  
  { OutOfOfficeMessage:  }  
  { MediumPhotoUrl: https://yourcompany63-dev-ed--c.documentforce.com/profilephoto/005/M }  
  { DigestFrequency: N }  
  { DefaultGroupNotificationFrequency: N }  
  { JigsawImportLimitOverride: None }  
  { LastViewedDate: 2021-12-18T15:24:59.000+0000 }  
  { LastReferencedDate: 2021-12-18T15:24:59.000+0000 }  
  { BannerPhotoUrl: /profilephoto/005/B }  
  { SmallBannerPhotoUrl: /profilephoto/005/D }  
  { MediumBannerPhotoUrl: /profilephoto/005/E }  
  { IsProfilePhotoActive: False }  
  { IndividualId: None }  
]

CONTACTS
[  { attributes: {'type': 'Contact', 'url': '/services/data/v45.0/sobjects/Contact/0035j00000AfzPMAAZ'} }  
  { Id: 0035j00000AfzPMAAZ }  
  { IsDeleted: False }  
  { MasterRecordId: None }  
  { AccountId: 0015j00000DzvF3AAJ }  
  { LastName: Levy }  
  { FirstName: Babara }  
  { Salutation: Ms. }  
  { Name: Babara Levy }  
  { OtherStreet: None }  
  { OtherCity: None }  
  { OtherState: None }  
  { OtherPostalCode: None }  
  { OtherCountry: None }  
  { OtherLatitude: None }  
  { OtherLongitude: None }  
  { OtherGeocodeAccuracy: None }  
  { OtherAddress: None }  
  { MailingStreet: 620 SW 5th Avenue Suite 400
Portland, Oregon 97204
United States }  
  { MailingCity: None }  
  { MailingState: None }  
  { MailingPostalCode: None }  
  { MailingCountry: None }  
  { MailingLatitude: None }  
  { MailingLongitude: None }  
  { MailingGeocodeAccuracy: None }  
  { MailingAddress: {'city': None, 'country': None, 'geocodeAccuracy': None, 'latitude': None, 'longitude': None, 'postalCode': None, 'state': None, 'street': '620 SW 5th Avenue Suite 400\nPortland, Oregon 97204\nUnited States'} }  
  { Phone: (503) 421-7800 }  
  { Fax: (503) 421-7801 }  
  { MobilePhone: (503) 421-5451 }  
  { HomePhone: None }  
  { OtherPhone: None }  
  { AssistantPhone: (503) 421-6782 }  
  { ReportsToId: None }  
  { Email: b.levy@expressl&t.net }  
  { Title: SVP, Operations }  
  { Department: Operations }  
  { AssistantName: Ron Sage }  
  { LeadSource: Word of mouth }  
  { Birthdate: 1938-11-06 }  
  { Description: None }  
  { OwnerId: 0055j000002oWyfAAE }  
  { CreatedDate: 2021-12-17T13:50:14.000+0000 }  
  { CreatedById: 0055j000002oWyfAAE }  
  { LastModifiedDate: 2021-12-17T13:50:14.000+0000 }  
  { LastModifiedById: 0055j000002oWyfAAE }  
  { SystemModstamp: 2021-12-17T13:50:14.000+0000 }  
  { LastActivityDate: None }  
  { LastCURequestDate: None }  
  { LastCUUpdateDate: None }  
  { LastViewedDate: 2021-12-18T15:24:56.000+0000 }  
  { LastReferencedDate: 2021-12-18T15:24:56.000+0000 }  
  { EmailBouncedReason: None }  
  { EmailBouncedDate: None }  
  { IsEmailBounced: False }  
  { PhotoUrl: /services/images/photo/0035j00000AfzPMAAZ }  
  { Jigsaw: None }  
  { JigsawContactId: None }  
  { CleanStatus: Pending }  
  { IndividualId: None }  
  { Level__c: Primary }  
  { Languages__c: English }  
]


"""