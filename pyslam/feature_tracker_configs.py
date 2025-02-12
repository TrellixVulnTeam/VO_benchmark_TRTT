"""
* This file is part of PYSLAM 
*
* Copyright (C) 2016-present Luigi Freda <luigi dot freda at gmail dot com> 
*
* PYSLAM is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* PYSLAM is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with PYSLAM. If not, see <http://www.gnu.org/licenses/>.
"""

from feature_tracker import feature_tracker_factory, FeatureTrackerTypes 
from feature_manager import feature_manager_factory
from feature_types import FeatureDetectorTypes, FeatureDescriptorTypes, FeatureInfo
from feature_matcher import feature_matcher_factory, FeatureMatcherTypes

from parameters import Parameters  


# some default parameters 

kNumFeatures=Parameters.kNumFeatures    

kRatioTest=Parameters.kFeatureMatchRatioTest

kTrackerType = FeatureTrackerTypes.DES_BF      # default descriptor-based, brute force matching with knn 
#kTrackerType = FeatureTrackerTypes.DES_FLANN  # default descriptor-based, FLANN-based matching 
        
        
"""
A collection of ready-to-used feature tracker configurations 
"""
class FeatureTrackerConfigs(object):   
    
    # Test/Template configuration: you can use this to quickly test 
    # - your custom parameters and 
    # - favourite descriptor and detector (check the file feature_types.py)
    TEST = dict(num_features=kNumFeatures,                   
                num_levels = 8,                                  # N.B: some detectors/descriptors do not allow to set num_levels or they set it on their own
                scale_factor = 1.2,                              # N.B: some detectors/descriptors do not allow to set scale_factor or they set it on their own
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.ORB2, 
                match_ratio_test = kRatioTest,
                tracker_type = kTrackerType)
    
    ######################################################
    #################### TEST CONFIG COMBINATION #########
    ######################################################
    # Format: T[XX]_[YY]_[ZZ];
    # XX is test ID number
    # YY is detector name
    # ZZ is descriptor name
    # there are 42 combinations + some deep learning


    test_configs = { 
        'T01_SHI_NONE':dict(num_features=kNumFeatures,
                        num_levels = 3,
                        detector_type = FeatureDetectorTypes.SHI_TOMASI,
                        descriptor_type = FeatureDescriptorTypes.NONE, 
                        tracker_type = FeatureTrackerTypes.LK), # done

        'T02_SHI_SIFT':dict(num_features=kNumFeatures,
                        num_levels = 3,
                        detector_type = FeatureDetectorTypes.SHI_TOMASI,
                        descriptor_type = FeatureDescriptorTypes.SIFT, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T03_SHI_SURF':dict(num_features=kNumFeatures,
                        num_levels = 3,
                        detector_type = FeatureDetectorTypes.SHI_TOMASI,
                        descriptor_type = FeatureDescriptorTypes.SURF, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T04_SHI_ORB2':dict(num_features=kNumFeatures,
                        num_levels = 3,
                        detector_type = FeatureDetectorTypes.SHI_TOMASI,
                        descriptor_type = FeatureDescriptorTypes.ORB2, 
                        match_ratio_test = kRatioTest,                        
                        tracker_type = kTrackerType), # done

        'T05_SHI_BRISK':dict(num_features=kNumFeatures,
                        num_levels = 3,
                        detector_type = FeatureDetectorTypes.SHI_TOMASI,
                        descriptor_type = FeatureDescriptorTypes.BRISK,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done

        'T06_SHI_TFEAT':dict(num_features=kNumFeatures,
                        num_levels = 3,
                        detector_type = FeatureDetectorTypes.SHI_TOMASI,
                        descriptor_type = FeatureDescriptorTypes.TFEAT,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done


        ## FAST detector + 6 descriptors
        'T07_FAST_NONE':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.FAST, 
                        descriptor_type = FeatureDescriptorTypes.NONE, 
                        tracker_type = FeatureTrackerTypes.LK), # done

        'T08_FAST_SIFT':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.FAST, 
                        descriptor_type = FeatureDescriptorTypes.SIFT, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T09_FAST_SURF':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.FAST,
                        descriptor_type = FeatureDescriptorTypes.SURF, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T10_FAST_ORB2':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.FAST,
                        descriptor_type = FeatureDescriptorTypes.ORB2, 
                        match_ratio_test = kRatioTest,                        
                        tracker_type = kTrackerType), # done

        'T11_FAST_BRISK':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.FAST,
                        descriptor_type = FeatureDescriptorTypes.BRISK,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done

        'T12_FAST_TFEAT':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.FAST,
                        descriptor_type = FeatureDescriptorTypes.TFEAT,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done

        ## SIFT detector + 6 descriptors
        'T13_SIFT_NONE':dict(num_features=kNumFeatures,  
                        detector_type = FeatureDetectorTypes.SIFT, 
                        descriptor_type = FeatureDescriptorTypes.NONE, 
                        tracker_type = FeatureTrackerTypes.LK), # done

        'TXX_SIFT_ORB2':dict(num_features=kNumFeatures,  
                        detector_type = FeatureDetectorTypes.SIFT,
                        descriptor_type = FeatureDescriptorTypes.ORB2, 
                        match_ratio_test = kRatioTest,                        
                        tracker_type = kTrackerType), # done
        
        
        'T14_SIFT_SIFT':dict(num_features=kNumFeatures,  
                        detector_type = FeatureDetectorTypes.SIFT, 
                        descriptor_type = FeatureDescriptorTypes.SIFT, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T15_SIFT_SURF':dict(num_features=kNumFeatures,  
                        detector_type = FeatureDetectorTypes.SIFT, 
                        descriptor_type = FeatureDescriptorTypes.SURF, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T16_SIFT_ORB2':dict(num_features=kNumFeatures,  
                        detector_type = FeatureDetectorTypes.SIFT, 
                        descriptor_type = FeatureDescriptorTypes.ORB2, 
                        match_ratio_test = kRatioTest,                        
                        tracker_type = kTrackerType), # done

        'T17_SIFT_BRISK':dict(num_features=kNumFeatures,  
                        detector_type = FeatureDetectorTypes.SIFT, 
                        descriptor_type = FeatureDescriptorTypes.BRISK,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done

        'T18_SIFT_TFEAT':dict(num_features=kNumFeatures,  
                        detector_type = FeatureDetectorTypes.SIFT, 
                        descriptor_type = FeatureDescriptorTypes.TFEAT,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done

        ## SURF detector + 6 descriptors
        'T19_SURF_NONE':dict(num_features=kNumFeatures,
                        num_levels = 8,
                        detector_type = FeatureDetectorTypes.SURF, 
                        descriptor_type = FeatureDescriptorTypes.NONE, 
                        tracker_type = FeatureTrackerTypes.LK), # done

        'T20_SURF_SIFT':dict(num_features=kNumFeatures,
                        num_levels = 8,
                        detector_type = FeatureDetectorTypes.SURF, 
                        descriptor_type = FeatureDescriptorTypes.SIFT, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T21_SURF_SURF':dict(num_features=kNumFeatures,
                        num_levels = 8,
                        detector_type = FeatureDetectorTypes.SURF, 
                        descriptor_type = FeatureDescriptorTypes.SURF, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T22_SURF_ORB2':dict(num_features=kNumFeatures,
                        num_levels = 8,
                        detector_type = FeatureDetectorTypes.SURF, 
                        descriptor_type = FeatureDescriptorTypes.ORB2, 
                        match_ratio_test = kRatioTest,                        
                        tracker_type = kTrackerType), # done

        'T23_SURF_BRISK':dict(num_features=kNumFeatures,
                        num_levels = 8,
                        detector_type = FeatureDetectorTypes.SURF, 
                        descriptor_type = FeatureDescriptorTypes.BRISK,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done

        'T24_SURF_TFEAT':dict(num_features=kNumFeatures,
                        num_levels = 8,
                        detector_type = FeatureDetectorTypes.SURF, 
                        descriptor_type = FeatureDescriptorTypes.TFEAT,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done

        ## ORB2 detector + 6 descriptors
        'T25_ORB2_NONE':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.ORB2, 
                        descriptor_type = FeatureDescriptorTypes.NONE, 
                        tracker_type = FeatureTrackerTypes.LK), # done

        'T26_ORB2_SIFT':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.ORB2, 
                        descriptor_type = FeatureDescriptorTypes.SIFT, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T27_ORB2_SURF':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.ORB2,
                        descriptor_type = FeatureDescriptorTypes.SURF, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T28_ORB2_ORB2':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.ORB2,
                        descriptor_type = FeatureDescriptorTypes.ORB2, 
                        match_ratio_test = kRatioTest,                        
                        tracker_type = kTrackerType), # done

        'T29_ORB2_BRISK':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.ORB2,
                        descriptor_type = FeatureDescriptorTypes.BRISK,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done

        'T30_ORB2_TFEAT':dict(num_features=kNumFeatures,  
                        num_levels = 8, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.ORB2,
                        descriptor_type = FeatureDescriptorTypes.TFEAT,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done

        ## BRISK detector + 6 descriptors
        'T31_BRISK_NONE':dict(num_features=kNumFeatures,  
                        num_levels = 4, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.BRISK, 
                        descriptor_type = FeatureDescriptorTypes.NONE, 
                        tracker_type = FeatureTrackerTypes.LK), # done

        'T32_BRISK_SIFT':dict(num_features=kNumFeatures,  
                        num_levels = 4, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.BRISK, 
                        descriptor_type = FeatureDescriptorTypes.SIFT, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T33_BRISK_SURF':dict(num_features=kNumFeatures,  
                        num_levels = 4, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.BRISK,
                        descriptor_type = FeatureDescriptorTypes.SURF, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T34_BRISK_ORB2':dict(num_features=kNumFeatures,  
                        num_levels = 4, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.BRISK,
                        descriptor_type = FeatureDescriptorTypes.ORB2, 
                        match_ratio_test = kRatioTest,                        
                        tracker_type = kTrackerType), # done

        'T35_BRISK_BRISK':dict(num_features=kNumFeatures,  
                        num_levels = 4, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.BRISK,
                        descriptor_type = FeatureDescriptorTypes.BRISK,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done

        'T36_BRISK_TFEAT':dict(num_features=kNumFeatures,  
                        num_levels = 4, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.BRISK,
                        descriptor_type = FeatureDescriptorTypes.TFEAT,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done

        ## KEYNET detector + 6 descriptors
        'T37_KEYNET_NONE':dict(num_features=kNumFeatures,  
                        num_levels = 1, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.KEYNET, 
                        descriptor_type = FeatureDescriptorTypes.NONE, 
                        tracker_type = FeatureTrackerTypes.LK), # done

        'T38_KEYNET_SIFT':dict(num_features=kNumFeatures,  
                        num_levels = 1, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.KEYNET, 
                        descriptor_type = FeatureDescriptorTypes.SIFT, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T39_KEYNET_SURF':dict(num_features=kNumFeatures,  
                        num_levels = 1, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.KEYNET,
                        descriptor_type = FeatureDescriptorTypes.SURF, 
                        match_ratio_test = kRatioTest,                         
                        tracker_type = kTrackerType), # done

        'T40_KEYNET_ORB2':dict(num_features=kNumFeatures,  
                        num_levels = 1, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.KEYNET,
                        descriptor_type = FeatureDescriptorTypes.ORB2, 
                        match_ratio_test = kRatioTest,                        
                        tracker_type = kTrackerType), # done

        'T41_KEYNET_BRISK':dict(num_features=kNumFeatures,  
                        num_levels = 1, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.KEYNET,
                        descriptor_type = FeatureDescriptorTypes.BRISK,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done

        'T42_KEYNET_TFEAT':dict(num_features=kNumFeatures,  
                        num_levels = 1, 
                        scale_factor = 1.2,
                        detector_type = FeatureDetectorTypes.KEYNET,
                        descriptor_type = FeatureDescriptorTypes.TFEAT,
                        match_ratio_test = kRatioTest,                           
                        tracker_type = kTrackerType), # done


        # Deep learning features with 1-1 map (cannot combine with others)
        # T50 - T53 has some template, and we can use as is.  
        'T50_SUPERPOINT':dict(num_features=kNumFeatures, 
                          num_levels = 1, 
                          scale_factor = 1.2,
                          detector_type = FeatureDetectorTypes.SUPERPOINT, 
                          descriptor_type = FeatureDescriptorTypes.SUPERPOINT, 
                          match_ratio_test = kRatioTest,                               
                          tracker_type = kTrackerType),

        'T51_CONTEXTDESC':dict(num_features=kNumFeatures,                   
                           num_levels = 1,                                  
                           scale_factor = 1.2,                              
                           detector_type = FeatureDetectorTypes.CONTEXTDESC, 
                           descriptor_type = FeatureDescriptorTypes.CONTEXTDESC, 
                           match_ratio_test = kRatioTest,
                           tracker_type = kTrackerType),

        'T52_KEYNET':dict(num_features=kNumFeatures,                   
                           num_levels = 1,                                  
                           scale_factor = 1.2,                              
                           detector_type = FeatureDetectorTypes.KEYNET, 
                           descriptor_type = FeatureDescriptorTypes.KEYNET, 
                           match_ratio_test = kRatioTest,
                           tracker_type = kTrackerType),

        'T53_DISK':dict(num_features=kNumFeatures,                   
                           num_levels = 1,                                  
                           scale_factor = 1.2,                              
                           detector_type = FeatureDetectorTypes.DISK, 
                           descriptor_type = FeatureDescriptorTypes.DISK, 
                           match_ratio_test = kRatioTest,
                           tracker_type = kTrackerType),
        
        ## New DL features
        'T54_R2D2_R2D2':dict(num_features=kNumFeatures,                   
                           num_levels = 1,                                  
                           scale_factor = 1.2,                              
                           detector_type = FeatureDetectorTypes.R2D2, 
                           descriptor_type = FeatureDescriptorTypes.R2D2, 
                           match_ratio_test = kRatioTest,
                           tracker_type = kTrackerType),

        'T55_LFNET_LFNET':dict(num_features=kNumFeatures,                   
                           num_levels = 1,                                  
                           scale_factor = 1.2,                              
                           detector_type = FeatureDetectorTypes.LFNET, 
                           descriptor_type = FeatureDescriptorTypes.LFNET, 
                           match_ratio_test = kRatioTest,
                           tracker_type = kTrackerType),

        'T56_ORB2_VGG':dict(num_features=kNumFeatures,                   
                           num_levels = 8,                                  
                           scale_factor = 1.2,                              
                           detector_type = FeatureDetectorTypes.ORB2, 
                           descriptor_type = FeatureDescriptorTypes.VGG, 
                           match_ratio_test = kRatioTest,
                           tracker_type = kTrackerType),

        # orb and DL feats
        'T57_ORB2_HARDNET': dict(num_features=kNumFeatures, 
                             num_levels = 8, 
                             scale_factor = 1.2, 
                             detector_type = FeatureDetectorTypes.ORB2, 
                             descriptor_type = FeatureDescriptorTypes.HARDNET, 
                             match_ratio_test = kRatioTest,                        
                             tracker_type = kTrackerType),    

        'T58_ORB2_SOSNET': dict(num_features=kNumFeatures, 
                            num_levels = 8, 
                            scale_factor = 1.2, 
                            detector_type = FeatureDetectorTypes.ORB2, 
                            descriptor_type = FeatureDescriptorTypes.SOSNET, 
                            match_ratio_test = kRatioTest,                        
                            tracker_type = kTrackerType),   

        'T59_ORB2_L2NET': dict(num_features=kNumFeatures, 
                           num_levels = 8, 
                           scale_factor = 1.2, 
                           detector_type = FeatureDetectorTypes.ORB2, 
                           descriptor_type = FeatureDescriptorTypes.L2NET, 
                           match_ratio_test = kRatioTest,                        
                           tracker_type = kTrackerType),

        'T60_D2NET_D2NET':dict(num_features=kNumFeatures,                   
                   num_levels = 1,                                  
                   scale_factor = 1.2,                              
                   detector_type = FeatureDetectorTypes.D2NET, 
                   descriptor_type = FeatureDescriptorTypes.D2NET, 
                   match_ratio_test = kRatioTest,
                   tracker_type = kTrackerType),
        }

    
    
    # =====================================
    # LK trackers (these can only be used with VisualOdometry() ... at the present time)
    
    LK_SHI_TOMASI = dict(num_features=kNumFeatures,
                         num_levels = 3,
                         detector_type = FeatureDetectorTypes.SHI_TOMASI,
                         descriptor_type = FeatureDescriptorTypes.NONE, 
                         tracker_type = FeatureTrackerTypes.LK)

    LK_FAST = dict(num_features=kNumFeatures,
                   num_levels = 3,
                   detector_type = FeatureDetectorTypes.FAST, 
                   descriptor_type = FeatureDescriptorTypes.NONE, 
                   tracker_type = FeatureTrackerTypes.LK)


    # =====================================
    # Descriptor-based 'trackers' 
    
    SHI_TOMASI_ORB = dict(num_features=kNumFeatures,                   # N.B.: here, keypoints are not oriented! (i.e. keypoint.angle=0 always)
                          num_levels = 8, 
                          scale_factor = 1.2,
                          detector_type = FeatureDetectorTypes.SHI_TOMASI, 
                          descriptor_type = FeatureDescriptorTypes.ORB, 
                          match_ratio_test = kRatioTest,
                          tracker_type = kTrackerType)
    
    SHI_TOMASI_FREAK = dict(num_features=kNumFeatures,                     
                            num_levels=8,                      
                            scale_factor = 1.2,
                            detector_type = FeatureDetectorTypes.SHI_TOMASI, 
                            descriptor_type = FeatureDescriptorTypes.FREAK, 
                            match_ratio_test = kRatioTest,
                            tracker_type = kTrackerType)      

    FAST_ORB = dict(num_features=kNumFeatures,                         # N.B.: here, keypoints are not oriented! (i.e. keypoint.angle=0 always)
                    num_levels = 8, 
                    scale_factor = 1.2,
                    detector_type = FeatureDetectorTypes.FAST, 
                    descriptor_type = FeatureDescriptorTypes.ORB, 
                    match_ratio_test = kRatioTest,                         
                    tracker_type = kTrackerType) 
    
    FAST_FREAK = dict(num_features=kNumFeatures,                       
                      num_levels = 8,
                      scale_factor = 1.2,                    
                      detector_type = FeatureDetectorTypes.FAST, 
                      descriptor_type = FeatureDescriptorTypes.FREAK,      
                      match_ratio_test = kRatioTest,                          
                      tracker_type = kTrackerType)       

    BRISK = dict(num_features=kNumFeatures,                     
                num_levels = 4, 
                scale_factor = 1.2,
                detector_type = FeatureDetectorTypes.BRISK, 
                descriptor_type = FeatureDescriptorTypes.BRISK, 
                match_ratio_test = kRatioTest,                               
                tracker_type = kTrackerType)  
    
    BRISK_TFEAT = dict(num_features=kNumFeatures,                     
                       num_levels = 4, 
                       scale_factor = 1.2,
                       detector_type = FeatureDetectorTypes.BRISK, 
                       descriptor_type = FeatureDescriptorTypes.TFEAT, 
                       match_ratio_test = kRatioTest,                               
                       tracker_type = kTrackerType)        

    ORB = dict(num_features=kNumFeatures, 
               num_levels = 8, 
               scale_factor = 1.2, 
               detector_type = FeatureDetectorTypes.ORB, 
               descriptor_type = FeatureDescriptorTypes.ORB, 
               match_ratio_test = kRatioTest,                        
               tracker_type = kTrackerType)
    
    ORB2 = dict(num_features=kNumFeatures, 
                num_levels = 8, 
                scale_factor = 1.2, 
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.ORB2, 
                match_ratio_test = kRatioTest,                        
                tracker_type = kTrackerType)    
    
    BRISK = dict(num_features=kNumFeatures,
                 num_levels = 8,
                 detector_type = FeatureDetectorTypes.BRISK, 
                 descriptor_type = FeatureDescriptorTypes.BRISK,
                 match_ratio_test = kRatioTest,                           
                 tracker_type = kTrackerType)   

    KAZE = dict(num_features=kNumFeatures,
                num_levels = 8,
                detector_type = FeatureDetectorTypes.KAZE, 
                descriptor_type = FeatureDescriptorTypes.KAZE, 
                match_ratio_test = kRatioTest,                          
                tracker_type = kTrackerType)  
    
    AKAZE = dict(num_features=kNumFeatures,
                 num_levels = 8,
                 detector_type = FeatureDetectorTypes.AKAZE, 
                 descriptor_type = FeatureDescriptorTypes.AKAZE, 
                 match_ratio_test = kRatioTest,                          
                 tracker_type = kTrackerType)  
                
    SIFT = dict(num_features=kNumFeatures,
                detector_type = FeatureDetectorTypes.SIFT, 
                descriptor_type = FeatureDescriptorTypes.SIFT, 
                match_ratio_test = kRatioTest,                         
                tracker_type = kTrackerType)
    
    ROOT_SIFT = dict(num_features=kNumFeatures,
                     detector_type = FeatureDetectorTypes.ROOT_SIFT, 
                     descriptor_type = FeatureDescriptorTypes.ROOT_SIFT, 
                     match_ratio_test = kRatioTest,                              
                     tracker_type = kTrackerType)    
    
    # NOTE: SURF is a patented algorithm and not included in the new opencv versions 
    #       If you want to test it, you can install and old version of opencv that supports it: run 
    #       $ pip3 uninstall opencv-contrib-python
    #       $ pip3 install opencv-contrib-python==3.4.2.16
    SURF = dict(num_features=kNumFeatures,
                num_levels = 8,
                detector_type = FeatureDetectorTypes.SURF, 
                descriptor_type = FeatureDescriptorTypes.SURF, 
                match_ratio_test = kRatioTest,                         
                tracker_type = kTrackerType)
        
    SUPERPOINT = dict(num_features=kNumFeatures,                            # N.B.: here, keypoints are not oriented! (i.e. keypoint.angle=0 always)
                      num_levels = 1, 
                      scale_factor = 1.2,
                      detector_type = FeatureDetectorTypes.SUPERPOINT, 
                      descriptor_type = FeatureDescriptorTypes.SUPERPOINT, 
                      match_ratio_test = kRatioTest,                               
                      tracker_type = kTrackerType)

    CONTEXTDESC = dict(num_features=kNumFeatures,                   
                       num_levels = 1,                                  
                       scale_factor = 1.2,                              
                       detector_type = FeatureDetectorTypes.CONTEXTDESC, 
                       descriptor_type = FeatureDescriptorTypes.CONTEXTDESC, 
                       match_ratio_test = kRatioTest,
                       tracker_type = kTrackerType)
    
    KEYNET = dict(num_features=kNumFeatures,                   
                       num_levels = 1,                                  
                       scale_factor = 1.2,                              
                       detector_type = FeatureDetectorTypes.KEYNET, 
                       descriptor_type = FeatureDescriptorTypes.KEYNET, 
                       match_ratio_test = kRatioTest,
                       tracker_type = kTrackerType)
        
    DISK = dict(num_features=kNumFeatures,                   
                       num_levels = 1,                                  
                       scale_factor = 1.2,                              
                       detector_type = FeatureDetectorTypes.DISK, 
                       descriptor_type = FeatureDescriptorTypes.DISK, 
                       match_ratio_test = kRatioTest,
                       tracker_type = kTrackerType)
    
    # =====================================
    # Descriptor-based 'trackers' with ORB2
    
    ORB2_FREAK = dict(num_features=kNumFeatures, 
                      num_levels = 8, 
                      scale_factor = 1.2,                     
                      detector_type = FeatureDetectorTypes.ORB2, 
                      descriptor_type = FeatureDescriptorTypes.FREAK, 
                      match_ratio_test = kRatioTest,                        
                      tracker_type = kTrackerType)    
    
    ORB2_BEBLID = dict(num_features=kNumFeatures, 
                num_levels = 8, 
                scale_factor = 1.2, 
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.BEBLID, 
                match_ratio_test = kRatioTest,                        
                tracker_type = kTrackerType)    
    
    ORB2_HARDNET = dict(num_features=kNumFeatures, 
                num_levels = 8, 
                scale_factor = 1.2, 
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.HARDNET, 
                match_ratio_test = kRatioTest,                        
                tracker_type = kTrackerType)    
    
    ORB2_SOSNET = dict(num_features=kNumFeatures, 
                num_levels = 8, 
                scale_factor = 1.2, 
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.SOSNET, 
                match_ratio_test = kRatioTest,                        
                tracker_type = kTrackerType)   
    
    ORB2_L2NET = dict(num_features=kNumFeatures, 
                num_levels = 8, 
                scale_factor = 1.2, 
                detector_type = FeatureDetectorTypes.ORB2, 
                descriptor_type = FeatureDescriptorTypes.L2NET, 
                match_ratio_test = kRatioTest,                        
                tracker_type = kTrackerType) 
