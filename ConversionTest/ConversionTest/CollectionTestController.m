//
//  CollectionTestController.m
//  ConversionTest
//
//  Created by Alexander Maltsev on 3/19/16.
//  Copyright © 2016 self. All rights reserved.
//

#import "CollectionTestController.h"

@interface CollectionTestController () <UICollectionViewDataSource>

@property (weak, nonatomic) IBOutlet UICollectionView *collectionView;

@end

@implementation CollectionTestController

- (void)viewDidLoad
{
    [super viewDidLoad];
    // Do any additional setup after loading the view.
}


- (NSInteger)collectionView:(UICollectionView *)collectionView numberOfItemsInSection:(NSInteger)section
{
    return 0;
}


- (UICollectionViewCell *)collectionView:(UICollectionView *)collectionView cellForItemAtIndexPath:(NSIndexPath *)indexPath
{
    return nil;
}

@end
