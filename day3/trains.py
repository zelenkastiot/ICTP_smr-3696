from tqdm import tqdm

class Parcel:
    def __init__(self, weight, destination, status=True):
        self.weight = weight
        self.destination = destination
        self.status = status


    def get_weight(self):
        return self.weight
    
    def get_destination(self):
        return self.destination

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
        
    def __str__(self):
        return f"\n{self.destination} {self.weight}"


class Train:
    def __init__(self, capacity, train_destination, parcels_on_train=[], status=False):
        self.capacity = capacity
        self.train_destination = train_destination
        self.parcels_on_train = parcels_on_train
        self.status = status
    
    def get_parcels_on_train(self):
        return self.parcels_on_train
    
    def get_fill_rate(self):
        """
        Return the current fill rate of Train
        """
        if len(self.parcels_on_train) == 0:
            return 0

        return sum([pkg.weight for pkg in self.parcels_on_train])


    def can_send(self, package):
        """
        Return if the package can be added to the train
        """
        if package.destination == self.train_destination:
            if package.weight + self.get_fill_rate() <= self.capacity:
                return True

        return False

    def can_depart(self):
        return self.capacity == self.get_fill_rate()

    def depart(self):
        self.status = True

    def set_parcels_on_train(self, new_list):
        """
        Add package to train
        """
        self.parcels_on_train = new_list
        
    def __str__(self):
        return f"\nTrain {self.get_fill_rate()}/{self.capacity} destination {self.train_destination}"

class Platform:
    def __init__(self, list_packages, list_trains):
        self.list_packages = list_packages
        self.list_trains = list_trains
        
    def list_my_pkgs(self):
        for pkg in self.list_packages:
            print(pkg)

    def list_my_trains(self):
        for train in self.list_trains:
            print(train)
            print(train.parcels_on_train)
    
    def start_package_check(self):

        for train in self.list_trains:
            
            print(train)
            print(train.get_parcels_on_train())
            
            print(sum([pkg.status for pkg in self.list_packages]))
            
            for pkg in self.list_packages:
                    if pkg.get_status(): 
                        if train.can_send(pkg):
                            pkg.set_status(False)
                            print(pkg)
                            train.set_parcels_on_train(train.get_parcels_on_train() + [pkg])
                            print(f"Added pkg with weight {pkg.weight} on train {train.get_fill_rate()}/{train.capacity}")

                    if train.can_depart():
                        train.depart()
                        print(f"Train departed with rate {train.get_fill_rate()}/{train.capacity}")
                        break

if __name__ == "__main__":
    
    parcels_files = open('parcels.txt', 'r')
    Lines = [l.strip() for l in parcels_files.readlines()]
    list_packages = []
    
    for i in tqdm(range(1, len(Lines))):
        pkg_destination, pkg_weight = Lines[i].split(" ")
        list_packages.append(Parcel(float(pkg_weight), pkg_destination))
        
       
    
    trains_files = open('trains.txt', 'r')
    Lines = [l.strip() for l in trains_files.readlines()]
    list_trains = []
                  
    for i in tqdm(range(1, len(Lines))):
        train_destination, train_capacity = Lines[i].split(" ")
        list_trains.append(Train(float(train_capacity)*1_000, train_destination))

    platform = Platform(list_packages, list_trains)

    platform.start_package_check()